# WoW Bone Mapper

Simple blender plugin that adds a additional toolkit to the WoW N-panel added by WowTools.

It allows you to select the armature of your choice, then at a press of a button you can instantly change the bone names from the default imported Indexed names (BoneXXX) to proper mirrored names (Arm_L).

## Workflow
Import M2I into blender.
Select the Armature of the model.
Press the button corresponding to said model. This will make the icon look pressed so you can see if its active.
Once you have done all your work and want to export it again. Hit the pressed button to reverse the mapping.

### Bonemap not available
I have only created a handful of bonemaps to come with the addon by default. Any additional ones you have to create yourself.
Doing so is simple: 
1. Navigate to ``%Appdata%\Blender Foundation\Blender\5.1\scripts\addons\WowBoneMapper\bone_maps``
2. Create a new .py file or if you are making a new player model i suggest copying a pre existing one.
3. Name it whatever you want, If you aim to contribute it here, Please name it sensibly.
4. Use the following template structure to map the bones and set the label.
```
LABEL = "Velf & Belf"
TYPE = "Character"       # REQUIRED
SUBTYPE = "Female"      # OPTIONAL (can be None)
BONES = [
    #### Core Bones ####
    ("Bone001", "Root"),
    ## Upper Body ##
    ("Bone003", "Spine_1"),
    ("Bone011", "Spine_2"),
    # Left Arms
    ("Bone030", "Shoulder_L"),
    ("Bone040", "Arm_L"),
```
*While # is entirely optional for commenting it does help organisation and seeing where things is.*
Contributions with additional bone maps would be very welcome! Simply open an issue so people know you are working on it and then later a pull request when you are ready to merge it.

### Reasons why you might want to do this
* Blenders mirror modifier now functions.
* Blenders built in X Modifier now works as intended.
* Vertex Painting is now a breeze.
* UV Mapping easier than ever.
* You can go drink a coffee with all the time you save from using mirroring features