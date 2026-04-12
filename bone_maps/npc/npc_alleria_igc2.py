# REQUIRED FIELDS:
LABEL = "Alleria IGC 2"
TYPE = "Cinematic"
# OPTIONAL FIELDS: (can be None)
SUBTYPE = "npc"
M2 = [
    "igc_alleria2",
]

BONES = [
    #### Core Bones ####
    ("Bone000", "Root"),
    ## Upper Body ##
    ("Bone003", "Spine_1"),
    ("Bone020", "Spine_2"),
    ("Bone038", "Spine_3"),
    ("Bone054", "Spine_4"),
    ("Bone001", "Spine_5"),
    ("Bone015", "Neck_1"),
    ("Bone032", "Neck_2"),
    ("Bone049", "Neck_3"),
    ("Bone060", "Head"),


    # Left Arms
    ("Bone016", "Shoulder_L"),
    ("Bone033", "Arm_1_L"),
    ("Bone050", "Arm_2_L"),
    ("Bone061", "Arm_3_L"),
    ("Bone125", "Arm_4_L"),
    ("Bone181", "Arm_5_L"),
    ("Bone197", "Arm_6_L"),
    ("Bone210", "Hand_L"),
    # Right Arms
    ("Bone017", "Shoulder_R"),
    ("Bone035", "Arm_1_R"),
    ("Bone051", "Arm_2_R"),
    ("Bone062", "Arm_3_R"),
    ("Bone126", "Arm_4_R"),
    ("Bone182", "Arm_5_R"),
    ("Bone198", "Arm_6_R"),
    ("Bone211", "Hand_R"),


    # Breasts
    ("Bone127", "Breast_L"),
    ("Bone183", "Breast_R"),


    ### Lower body ##
    ## Core Legs
    # Left Side
    ("Bone002", "Leg_1_L"),
    ("Bone019", "Leg_2_L"),
    ("Bone037", "Leg_3_L"),
    ("Bone053", "Leg_4_L"),
    ("Bone064", "Leg_5_L"),
    ("Bone128", "Leg_6_L"),
    ("Bone184", "Foot_L"),
    ("Bone199", "Toe_L"),
    # Right Side
    ("Bone012", "Leg_1_R"),
    ("Bone029", "Leg_2_R"),
    ("Bone047", "Leg_3_R"),
    ("Bone059", "Leg_4_R"),
    ("Bone066", "Leg_5_R"),
    ("Bone129", "Leg_6_R"),
    ("Bone185", "Foot_R"),
    ("Bone200", "Toe_R"),


    ### Extra Bones ###
    ## Cape
    ("Bone036", "Cape_1"),
    ("Bone052", "Cape_2"),
    ("Bone063", "Cape_3"),
    # ...
]