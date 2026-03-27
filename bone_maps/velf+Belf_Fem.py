LABEL = "Void Elf & Blood Elf"
TYPE = "Character"       # REQUIRED
SUBTYPE = "Female"      # OPTIONAL (can be None)

BONES = [
    #### Core Bones ####
    ("Bone001", "Root"),
    ## Upper Body ##
    ("Bone003", "Spine_1"),
    ("Bone009", "Spine_2"),
    ("Bone016", "Spine_3"),
    ("Bone025", "Neck1"),
    ("Bone032", "Neck2"),
    ("Bone042", "Head"),
    # Left Arms
    ("Bone021", "Shoulder_L"),
    ("Bone029", "Arm_L"),
    ("Bone037", "ForeArm_L"),
    ("Bone044", "Hand_L"),
    # Right Arms
    ("Bone022", "Shoulder_R"),
    ("Bone030", "Arm_R"),
    ("Bone038", "ForeArm_R"),
    ("Bone049", "Hand_R"),

    ## Bend Arms
    # Arms_L Bend
    ("Bone036", "Bicep_L"),
    ("Bone035", "Elbow_L"),
    ("Bone045", "Wank_L"),
    ("Bone046", "Wrist_L"),
    # Arms_R Bend
    ("Bone040", "Bicep_R"),
    ("Bone039", "Elbow_R"),
    ("Bone047", "Wank_R"),
    ("Bone048", "Wrist_R"),

    # Breasts
    ("Bone023", "Breast_L"),
    ("Bone026", "Breast_R"),


    ### Lower body ##
    ## Core Legs
    ("Bone002", "Pelvis"),
    # Left Side
    ("Bone008", "Thigh_L"),
    ("Bone014", "Calf_L"),
    ("Bone028", "Foot_L"),
    ("Bone034", "Toe_L"),
    # Right Side
    ("Bone006", "Thigh_R"),
    ("Bone013", "Calf_R"),
    ("Bone027", "Foot_R"),
    ("Bone033", "Toe_R"),

    ## Bend Legs
    # Leg_L Bend
    ("Bone015", "Knee_L"),
    ("Bone020", "Ankle_L"),

    # Leg_R Bend
    ("Bone012", "Knee_R"),
    ("Bone019", "Ankle_R"),

    ### Extra Bones ###
    ## Tabard
    # Front
    ("Bone004", "FrontTabard_1"),
    ("Bone010", "FrontTabard_2"),
    ("Bone017", "FrontTabard_3"),
    # Back
    ("Bone005", "BackTabard_1"),
    ("Bone011", "BackTabard_2"),
    ("Bone018", "BackTabard_3"),

    ## Cape
    ("Bone024", "Cape_1"),
    ("Bone031", "Cape_2"),
    ("Bone041", "Cape_3"),
    ("Bone050", "Cape_4"),
    ("Bone116", "Cape_5"),
    # ...
]