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
import pkgutil
from pathlib import Path

# ---------------------------------------------------------------------------
# Preset loading
# ---------------------------------------------------------------------------

def _load_bone_maps() -> list[dict]:
    """
    Scan the 'bone_maps' sub-package and return a list of bone map dicts.
    Each bone map file must define:
        LABEL : str   — button / section label shown in the panel
        BONES : list  — list of ("IndexedName", "MirroredName") tuples

    Files are loaded in filename order, so prefix with numbers to control
    button order:  01_void_elf.py, 02_human_male.py …
    """
    bone_maps = []
    bone_maps_pkg_name = f"{__name__}.bone_maps"

    try:
        bone_maps_pkg = importlib.import_module(bone_maps_pkg_name)
    except ModuleNotFoundError:
        # bone_maps/ folder doesn't exist yet — return empty list gracefully
        return bone_maps

    # __file__ is None for namespace packages (no __init__.py inside bone_maps/).
    # __path__ always exists and points at the folder directly.
    if bone_maps_pkg.__file__ is not None:
        bone_maps_path = Path(bone_maps_pkg.__file__).parent
    else:
        bone_maps_path = Path(list(bone_maps_pkg.__path__)[0])

    for finder, module_name, _ in sorted(pkgutil.iter_modules([str(bone_maps_path)])):
        full_name = f"{bone_maps_pkg_name}.{module_name}"
        try:
            mod = importlib.import_module(full_name)

            label = getattr(mod, "LABEL", module_name.replace("_", " ").title())
            bones = getattr(mod, "BONES", [])

            # ---- NEW ----
            armature_type = getattr(mod, "TYPE", None)
            if not armature_type:
                raise ValueError(f"{module_name} is missing required 'TYPE'")

            subtype = getattr(mod, "SUBTYPE", None)

            bone_maps.append({
                "id": module_name,
                "label": label,
                "bones": bones,
                "type": armature_type,
                "subtype": subtype,
                "mod": mod,
            })


        except Exception as e:
            print(f"[Bone Mapper] Failed to load bone map '{full_name}': {e}")

    return bone_maps


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

    # Decide based on majority
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

        # Find the matching bone map
        bone_map = next((m for m in _BONE_MAPS if m["id"] == self.bone_map_id), None)
        if bone_map is None:
            self.report({'ERROR'}, f"Bone map not found: '{self.bone_map_id}'")
            return {'CANCELLED'}

        bones = bone_map["bones"]
        to_mirrored = not _is_using_mirrored_names(armature, bones)
        count = _rename_bones(armature, bones, to_mirrored)

        # ---- NEW: store active preset ----
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
    bl_category = "WoW"             # WowTools already adds a Npanel. So it slots into that.

    def draw(self, context):
        layout = self.layout
        armature = _get_armature(context)

        # Armature status
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

        # Reload button at the bottom
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