bl_info = {
    "name": "Bone-Mapper",
    "author": "Dytser",
    "version": (1, 0, 0),
    "blender": (5, 0, 0),
    "location": "View3D > N Panel > Wow > Bone-Mapper",
    "description": "Toggle bone names between indexed (BoneXXX) and mirrored names (Arm_L)",
    "category": "Rigging",
}

import bpy
import importlib
import importlib.util
import pkgutil
from pathlib import Path

# ---------------------------------------------------------------------------
# Preset loading
# ---------------------------------------------------------------------------

def _load_bone_maps_from_path(directory: Path, package_prefix: str) -> list[dict]:
    """
    Recursively scan a directory for bone map .py files.
    Subfolders are traversed automatically — no __init__.py required inside them.
    Each .py file must define:
        LABEL : str   — button / section label shown in the panel
        BONES : list  — list of ("IndexedName", "MirroredName") tuples
        TYPE  : str   — required armature type (e.g. "Human", "Creature")
        SUBTYPE : str — optional subtype (e.g. "Female", "Male")
    """
    bone_maps = []

    for item in sorted(directory.iterdir()):
        if item.is_dir():
            # Recurse into subfolder — subfolders don't need an __init__.py
            bone_maps.extend(
                _load_bone_maps_from_path(item, f"{package_prefix}.{item.name}")
            )
        elif item.suffix == ".py" and item.stem != "__init__":
            module_name = f"{package_prefix}.{item.stem}"
            try:
                spec = importlib.util.spec_from_file_location(module_name, item)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)

                label = getattr(mod, "LABEL", item.stem.replace("_", " ").title())
                bones = getattr(mod, "BONES", [])

                armature_type = getattr(mod, "TYPE", None)
                if not armature_type:
                    raise ValueError(f"{item.name} is missing required 'TYPE'")

                subtype = getattr(mod, "SUBTYPE", None)

                bone_maps.append({
                    "id": module_name,          # now unique across subfolders
                    "label": label,
                    "bones": bones,
                    "type": armature_type,
                    "subtype": subtype,
                    "mod": mod,
                })

            except Exception as e:
                print(f"[Bone Mapper] Failed to load bone map '{item}': {e}")

    return bone_maps


def _load_bone_maps() -> list[dict]:
    """Entry point: locate the bone_maps folder and kick off recursive loading."""
    bone_maps_dir = Path(__file__).parent / "bone_maps"
    if not bone_maps_dir.is_dir():
        return []

    return _load_bone_maps_from_path(bone_maps_dir, f"{__name__}.bone_maps")


# Loaded once at registration; also refreshed on demand via the operator.
_BONE_MAPS: list[dict] = []


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_armature(context):
    obj = context.active_object
    if obj and obj.type == 'ARMATURE':
        return obj
    for ob in context.selected_objects:
        if ob.type == 'ARMATURE':
            return ob
    return None


def _rename_bones(armature_obj, bones: list, to_mirrored: bool) -> int:
    bone_data = armature_obj.data.bones
    renamed = 0
    for indexed, mirrored in bones:
        src = indexed  if to_mirrored else mirrored
        dst = mirrored if to_mirrored else indexed
        if src in bone_data:
            bone_data[src].name = dst
            renamed += 1
    return renamed


def _is_using_mirrored_names(armature_obj, bones: list) -> bool:
    if not bones:
        return False

    bone_data = armature_obj.data.bones

    mirrored_count = 0
    indexed_count = 0

    for indexed, mirrored in bones:
        if mirrored in bone_data:
            mirrored_count += 1
        if indexed in bone_data:
            indexed_count += 1

    return mirrored_count > indexed_count


def _group_bone_maps(bone_maps):
    grouped = {}
    for m in bone_maps:
        t = m["type"]
        g = m["subtype"] or "Unknown"

        grouped.setdefault(t, {})
        grouped[t].setdefault(g, [])
        grouped[t][g].append(m)

    return grouped


# ---------------------------------------------------------------------------
# Operators
# ---------------------------------------------------------------------------

class BONEMAPPER_OT_toggle(bpy.types.Operator):
    """Toggle bone names between indexed and mirrored for a given bone map."""
    bl_idname = "bone_mapper.toggle"
    bl_label = "Toggle Bone Names"
    bl_options = {'REGISTER', 'UNDO'}

    bone_map_id: bpy.props.StringProperty()

    def execute(self, context):
        armature = _get_armature(context)
        if armature is None:
            self.report({'WARNING'}, "No armature selected or active.")
            return {'CANCELLED'}

        bone_map = next((m for m in _BONE_MAPS if m["id"] == self.bone_map_id), None)
        if bone_map is None:
            self.report({'ERROR'}, f"Bone map not found: '{self.bone_map_id}'")
            return {'CANCELLED'}

        bones = bone_map["bones"]
        to_mirrored = not _is_using_mirrored_names(armature, bones)
        count = _rename_bones(armature, bones, to_mirrored)

        if to_mirrored:
            armature["bone_mapper_active"] = self.bone_map_id
        else:
            if armature.get("bone_mapper_active") == self.bone_map_id:
                del armature["bone_mapper_active"]

        direction = "Indexed → Mirrored" if to_mirrored else "Mirrored → Indexed"
        self.report({'INFO'}, f"[{bone_map['label']}] {direction}: {count} bone(s) renamed on '{armature.name}'.")
        return {'FINISHED'}


class BONEMAPPER_OT_reload(bpy.types.Operator):
    """Reload all bone map files from the bone_maps folder (no restart needed)."""
    bl_idname = "bone_mapper.reload"
    bl_label = "Reload Bone Maps"
    bl_options = {'REGISTER'}

    def execute(self, context):
        global _BONE_MAPS
        _BONE_MAPS = _load_bone_maps()
        self.report({'INFO'}, f"Bone Mapper: loaded {len(_BONE_MAPS)} bone map(s).")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# Panel
# ---------------------------------------------------------------------------

class BONEMAPPER_PT_panel(bpy.types.Panel):
    bl_label = "Bone Mapper"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "WoW"

    def draw(self, context):
        layout = self.layout
        armature = _get_armature(context)

        box = layout.box()
        if armature:
            box.label(text=f"Armature: {armature.name}", icon='ARMATURE_DATA')
        else:
            box.label(text="No armature selected", icon='ERROR')

        layout.separator(type='LINE')

        if not _BONE_MAPS:
            layout.label(text="No bone maps found.", icon='INFO')
            layout.label(text="Add .py files to bone_maps/")
            layout.separator(type='LINE')
        else:
            grouped = _group_bone_maps(_BONE_MAPS)

            for bone_type, genders in grouped.items():
                box = layout.box()
                box.label(text=bone_type, icon='GROUP')

                for gender, maps in genders.items():
                    col = box.column(align=True)

                    if gender and gender != "Unknown":
                        col.label(text=gender, icon='USER')

                    for bone_map in maps:
                        if armature:
                            active_map = armature.get("bone_mapper_active")
                            using_mirrored = active_map == bone_map["id"]
                            btn_icon = 'LINENUMBERS_ON' if using_mirrored else 'MOD_MIRROR'
                        else:
                            using_mirrored = False
                            btn_icon = 'FILE_REFRESH'

                        op = col.operator(
                            BONEMAPPER_OT_toggle.bl_idname,
                            text=bone_map["label"],
                            icon=btn_icon,
                            depress=using_mirrored,
                        )
                        op.bone_map_id = bone_map["id"]

            layout.separator(type='LINE')

        layout.operator(
            BONEMAPPER_OT_reload.bl_idname,
            text="Reload Bone Maps",
            icon='FILE_REFRESH',
        )


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

CLASSES = (
    BONEMAPPER_OT_toggle,
    BONEMAPPER_OT_reload,
    BONEMAPPER_PT_panel,
)


def register():
    global _BONE_MAPS
    for cls in CLASSES:
        bpy.utils.register_class(cls)
    _BONE_MAPS = _load_bone_maps()


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)