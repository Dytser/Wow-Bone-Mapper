# REQUIRED FIELDS:
LABEL = "Alleria"
TYPE = "NPC"
# OPTIONAL FIELDS: (can be None)
SUBTYPE = "Female"
M2 = [
    "alleria3",
    # Add more filenames here if other models share this exact skeleton
]

BONES = [
    #### Core Bones ####
    ("Bone002", "Root"),
    ## Upper Body ##
    ("Bone004", "Spine_1"),
    ("Bone008", "Spine_2"),
    ("Bone013", "Spine_3"),
    ("Bone018", "Neck_1"),
    ("Bone025", "Neck_2"),
    ("Bone035", "Head"),


    # Left Arms
    ("Bone016", "Shoulder_L"),
    ("Bone022", "Arm_L"),
    ("Bone030", "ForeArm_L"),
    ("Bone037", "Hand_L"),
    # Right Arms
    ("Bone017", "Shoulder_R"),
    ("Bone023", "Arm_R"),
    ("Bone031", "ForeArm_R"),
    ("Bone042", "Hand_R"),

    ## Bend Arms
    # Arms_L Bend
    ("Bone029", "Bicep_L"),
    ("Bone028", "Elbow_L"),
    ("Bone038", "Wank_L"),
    ("Bone039", "Wrist_L"),
    # Arms_R Bend
    ("Bone033", "Bicep_R"),
    ("Bone032", "Elbow_R"),
    ("Bone040", "Wank_R"),
    ("Bone041", "Wrist_R"),

    # Breasts
    ("Bone127", "Breast_L"),
    ("Bone130", "Breast_R"),


    ### Lower body ##
    ## Core Legs
    ("Bone003", "Pelvis"),
    # Left Side
    ("Bone007", "Thigh_L"),
    ("Bone011", "Calf_L"),
    ("Bone021", "Foot_L"),
    ("Bone027", "Toe_L"),
    # Right Side
    ("Bone005", "Thigh_R"),
    ("Bone010", "Calf_R"),
    ("Bone020", "Foot_R"),
    ("Bone026", "Toe_R"),

    ## Bend Legs
    # Leg_L Bend
    ("Bone012", "Knee_L"),
    ("Bone015", "Ankle_L"),

    # Leg_R Bend
    ("Bone009", "Knee_R"),
    ("Bone014", "Ankle_R"),

    ### Extra Bones ###
    ## Cape
    ("Bone024", "Cape_1"),
    ("Bone034", "Cape_2"),
    ("Bone043", "Cape_3"),
    ("Bone103", "Cape_4"),
    ("Bone127", "Cape_5"),
    ("Bone130", "Cape_6"),
    # ...
]