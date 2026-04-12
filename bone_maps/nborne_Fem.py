# REQUIRED FIELDS:
LABEL = "Night Borne"
TYPE = "Character"
# OPTIONAL FIELDS: (can be None)
SUBTYPE = "Female"
M2 = [
    "nightbornefemale",
]

BONES = [
    #### Core Bones ####
    ("Bone001", "Root"),
    ## Upper Body ##
    ("Bone003", "Spine_1"),
    ("Bone009", "Spine_2"),
    ("Bone014", "Spine_3"),
    ("Bone025", "Neck1"),
    ("Bone032", "Neck2"),
    ("Bone042", "Head"),
    # Left Arms
    ("Bone022", "Shoulder_L"),
    ("Bone030", "Arm_L"),
    ("Bone038", "ForeArm_L"),
    ("Bone048", "Hand_L"),
    # Right Arms
    ("Bone021", "Shoulder_R"),
    ("Bone029", "Arm_R"),
    ("Bone035", "ForeArm_R"),
    ("Bone047", "Hand_R"),

    ## Bend Arms
    # Arms_L Bend
    ("Bone040", "Bicep_L"),
    ("Bone039", "Elbow_L"),
    ("Bone049", "Wank_L"),
    ("Bone050", "Wrist_L"),
    # Arms_R Bend
    ("Bone037", "Bicep_R"),
    ("Bone036", "Elbow_R"), 
    ("Bone045", "Wank_R"),
    ("Bone046", "Wrist_R"),

    # Breasts
    ("Bone023", "Breast_L"),
    ("Bone026", "Breast_R"),


    ### Lower body ##
    ## Core Legs
    ("Bone002", "Pelvis"),
    # Left Side
    ("Bone013", "Thigh_L"),
    ("Bone019", "Calf_L"),
    ("Bone034", "Foot_L"),
    ("Bone044", "Toe_L"),
    # Right Side
    ("Bone011", "Thigh_R"),
    ("Bone017", "Calf_R"),
    ("Bone033", "Foot_R"),
    ("Bone043", "Toe_R"),

    ## Bend Legs
    # Leg_L Bend
    ("Bone020", "Knee_L"),
    ("Bone028", "Ankle_L"),

    # Leg_R Bend
    ("Bone016", "Knee_R"),
    ("Bone027", "Ankle_R"),

    ### Extra Bones ###
    ## Tabard
    # Front
    ("Bone004", "FrontTabard_1"),
    ("Bone010", "FrontTabard_2"),
    ("Bone015", "FrontTabard_3"),
    # Back
    ("Bone006", "BackTabard_1"),
    ("Bone012", "BackTabard_2"),
    ("Bone018", "BackTabard_3"),

    ## Cape
    ("Bone024", "Cape_1"),
    ("Bone031", "Cape_2"),
    ("Bone041", "Cape_3"),
    ("Bone052", "Cape_4"),
    ("Bone112", "Cape_5"),
    # ...
]