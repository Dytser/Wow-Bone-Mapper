# REQUIRED FIELDS:
LABEL = "Name of the character/model this bone map applies to"
TYPE = "Type of model this bone map applies to (e.g. Character, NPC, Cinematic, etc.)"
# OPTIONAL FIELDS: (can be None)
SUBTYPE = "Optional subtype or additional categorization for the model."
M2 = [
    "name_of_m2_file",
    # Add more filenames here if other models share this exact skeleton. Sepeated with commas.
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
    ("Bone055", "Arm_L"),
    ("Bone054", "ForeArm_1_L"),
    ("Bone061", "ForeArm_2_L"),
    ("Bone065", "ForeArm_3_L"),
    ("Bone078", "ForeArm_4_L"),
    ("Bone149", "ForeArm_5_L"),
    ("Bone183", "Hand_L"),
    # Right Arms
    ("Bone052", "Shoulder_R"),
    ("Bone058", "Arm_R"),
    ("Bone057", "ForeArm_1_R"),
    ("Bone062", "ForeArm_2_R"),
    ("Bone066", "ForeArm_3_R"),
    ("Bone080", "ForeArm_4_R"),
    ("Bone150", "ForeArm_5_R"),
    ("Bone184", "Hand_R"),


    # Breasts
    ("Bone188", "Breast_L"),
    ("Bone186", "Breast_R"),


    ### Lower body ##
    ## Core Legs
    ("Bone003", "Pelvis"),
    # Left Side
    ("Bone006", "Thigh_L"),
    ("Bone005", "Calf_L"),
    ("Bone004", "Foot_L"),
    ("Bone022", "Toe_L"),
    # Right Side
    ("Bone009", "Thigh_R"),
    ("Bone008", "Calf_R"),
    ("Bone007", "Foot_R"),
    ("Bone023", "Toe_R"),


    ### Extra Bones ###
    ## Cape
    ("Bone059", "Cape_1"),
    ("Bone063", "Cape_2"),
    ("Bone067", "Cape_3"),
    # ...
]