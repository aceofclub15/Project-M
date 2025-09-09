default gender = ""

label start:
    jump sc_computer
    return



label sc_computer:
    "Please choose your character's gender (choice won't affect gameplay)"
    menu:
        "Male":
            $ gender = "Male"
            jump sc_mission_start
        "Female":
            $ gender = "Female"
            jump sc_mission_start
    return

