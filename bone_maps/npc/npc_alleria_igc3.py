# REQUIRED FIELDS:
LABEL = "Alleria IGC 3"
TYPE = "Cinematic"
# OPTIONAL FIELDS: (can be None)  
SUBTYPE = "npc"
M2 = [
    "igc_alleria3",
    # Add more filenames here if other models share this exact skeleton:
]

BONES = [
    #### Core Bones ####
    ("Bone000", "Root"),
    ## Upper Body ##
    ("Bone003", "Spine_1"),
    ("Bone021", "Spine_2"),
    ("Bone032", "Spine_3"),
    ("Bone041", "Spine_4"),
    ("Bone048", "Spine_5"),
    ("Bone050", "Neck_1"),
    ("Bone053", "Neck_2"),
    ("Bone060", "Neck_3"),
    ("Bone064", "Head"),


    # Left Arms
    ("Bone051", "Shoulder_L"),
    ("Bone055", "Arm_1_L"),
    ("Bone054", "Arm_2_L"),
    ("Bone061", "Arm_3_L"),
    ("Bone065", "Arm_4_L"),
    ("Bone078", "Arm_5_L"),
    ("Bone149", "Arm_6_L"),
    ("Bone183", "Hand_L"),
    # Right Arms
    ("Bone052", "Shoulder_R"),
    ("Bone058", "Arm_1_R"),
    ("Bone057", "Arm_2_R"),
    ("Bone062", "Arm_3_R"),
    ("Bone066", "Arm_4_R"),
    ("Bone080", "Arm_5_R"),
    ("Bone150", "Arm_6_R"),
    ("Bone184", "Hand_R"),


    # Breasts
    ("Bone188", "Breast_L"),
    ("Bone186", "Breast_R"),


    ### Lower body ##
    ## Core Legs
    ("Bone003", "Pelvis"),
    # Left Side
    ("Bone006", "Leg_1_L"),
    ("Bone005", "Leg_2_L"),
    ("Bone004", "Foot_L"),
    ("Bone022", "Toe_L"),
    # Right Side
    ("Bone009", "Leg_1_R"),
    ("Bone008", "Leg_2_R"),
    ("Bone007", "Foot_R"),
    ("Bone023", "Toe_R"),


    ### Extra Bones ###
    ## Cape
    ("Bone059", "Cape_1"),
    ("Bone063", "Cape_2"),
    ("Bone067", "Cape_3"),
    # ...
]