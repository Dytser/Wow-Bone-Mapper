# REQUIRED FIELDS:
LABEL = "Draenei + LF"
TYPE = "Character"
# OPTIONAL FIELDS: (can be None)
SUBTYPE = "Female"
M2 = [
    "draeneifemale_hd",
    "lightforgeddraeneifemale",
]

BONES = [
    #### Core Bones ####
    ("Bone001", "Root"),
    ## Upper Body ##
    ("Bone003", "Spine_1"),
    ("Bone011", "Spine_2"),
    ("Bone019", "Spine_3"),
    ("Bone031", "Neck_1"),
    ("Bone041", "Neck_2"),
    ("Bone052", "Head"),
    # Left Arms
    ("Bone030", "Shoulder_L"),
    ("Bone040", "Arm_L"),
    ("Bone049", "ForeArm_L"),
    ("Bone057", "Hand_L"),
    # Right Arms
    ("Bone027", "Shoulder_R"),
    ("Bone038", "Arm_R"),
    ("Bone045", "ForeArm_R"),
    ("Bone055", "Hand_R"),

    ## Bend Arms
    # Arms_L Bend
    ("Bone051", "Bicep_L"),
    ("Bone050", "Elbow_L"),
    ("Bone058", "Wank_L"),
    ("Bone059", "Wrist_L"),
    # Arms_R Bend
    ("Bone046", "Bicep_R"),
    ("Bone047", "Elbow_R"),
    ("Bone053", "Wank_R"),
    ("Bone054", "Wrist_R"),

    # Breasts
    ("Bone028", "Breast_L"),
    ("Bone032", "Breast_R"),


    ### Lower body ##
    ## Core Legs
    ("Bone002", "Pelvis"),
    # Left Side
    ("Bone006", "Thigh_L"),
    ("Bone015", "Calf_L"),
    ("Bone023", "Hoof_L"),
    ("Bone036", "Foot_L"),
    ("Bone043", "Toe_L"),
    # Right Side
    ("Bone005", "Thigh_R"),
    ("Bone014", "Calf_R"),
    ("Bone022", "Hoof_R"),
    ("Bone034", "Foot_R"),
    ("Bone042", "Toe_R"),

    ## Bend Legs
    # Leg_L Bend
    ("Bone016", "Knee_L"),
    ("Bone024", "HoofBend_L"),
    ("Bone035", "Ankle_L"),


    # Leg_R Bend
    ("Bone013", "Knee_R"),
    ("Bone021", "HoofBend_R"),
    ("Bone033", "Ankle_R"),

    ### Extra Bones ###
    ## Tabard
    # Front
    ("Bone004", "FrontTabard_1"),
    ("Bone012", "FrontTabard_2"),
    ("Bone020", "FrontTabard_3"),
    # Back
    ("Bone007", "BackTabard_1"),
    ("Bone017", "BackTabard_2"),
    ("Bone025", "BackTabard_3"),

    ## Cape
    ("Bone029", "Cape_1"),
    ("Bone039", "Cape_2"),
    ("Bone048", "Cape_3"),
    ("Bone056", "Cape_4"),
    ("Bone108", "Cape_5"),
    # ...
]