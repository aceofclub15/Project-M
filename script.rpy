default gender = ""
define Grandmaster = Character("Grandmaster", color="#e5ff00")
define Crew_member = Character("Crewmember")


label start:
    jump sc_computer
    return



label sc_computer:
    scene black
    "Please choose your character's gender (choice won't affect gameplay)"
    menu:
        "Male":
            $ gender = "Male"
            jump sc_mission_archive
        "Female":
            $ gender = "Female"
            jump sc_mission_archive
    return



label sc_mission_archive:
    scene black 
    show hologram_GM:
        xalign 0.5
        yalign 0.5
    Grandmaster "How are you feeling, Enforcer XIII?"
    Morgan "I'm feeling as ready as I'll ever be."
    Grandmaster "Good, because time is of the essence. The assassin should've already infiltrated the hotel."
    Morgan "And I imagine Graham is making his move too?"
    Grandmaster "Indeed, I have him on radar. It won't take long for him to arrive."
    Morgan "Are you sure you want to leave everything to me, Grandmaster?"
    Grandmaster "I am. This is your story, Morgan. I only need one thing from you."
    Morgan "That's right. I just need to make things interesting."
    Grandmaster "You catch on well."
    Morgan "Looks like we've arrived at the hotel. This is where I get out."
    Grandmaster "All the best, Morgan. I know you'll make me proud."
    Morgan "I aim to please, Grandmaster."

    jump sc_hotel_entrance

    return

label sc_hotel_entrance:
    show bg hotel_entrance
    show Morgan_default
    Morgan "{i}According to the Grandmaster\'s intel, Triplex CEO Adam Rourke will be attending the \'Future of the Extranet\' conference in the 2nd Conference Hall, 90 minutes from now.{/i}"
    Morgan "{i}Now, how should I take control of this situation?{/i}"

    menu:
        "Declare an emergency":
            jump sc_emergency
        "Get hold of the guest list":
            jump sc_guest_list

    return
label sc_emergency:
    show bg emergency_room
    Hide Morgan_default
    Morgan "Attention everyone! This is Officer Morgan of the FBI! I\'m declaring a terroristic threat at the Charleston!" 
    Morgan "I need everyone to please-No wait, wait, don\'t escort me out, NOOOO!"

    "..."
    Grandmaster "You made a terrible judgment call, Morgan." 
    Grandmaster "By attracting undue attention to yourself, you\'ve ensured that
    you\'ll be arrested and charged for impersonating a Federal officer."
    Grandmaster " As for Adam Rourke, he was assassinated, but the assassin did a sloppy enough job to get arrested as well."
    Grandmaster "An incredibly boring and anti-climactic way to end things."
    Grandmaster "I\'m disappointed."

    "..."
    jump sc_hotel_entrance

    return

label sc_guest_list:
    Morgan "{i}That's right, I need to do this discreetly. If I get too many eyes on me, this mission's already a failure.{/i}"

    Morgan "Hi, excuse me! I'm Hendricks, from logistics. I just need to cross-check the guest list and make sure there are no empty tables at the 2nd Conference Hall. You know how the bosses are about wasted money."

    Crew member "Oh, I do, believe me. Here, take this flash drive. It should have everything you need to know about the Extranet conference."

    Morgan "Oh thank you, you're a lifesaver!"

    Morgan "{i}Now, time to plug in the drive and see.{/i}"

    Morgan "{i}It's as I suspected. This list has been tampered with. There's at least one person who isn't supposed to be here, but I'll need to do a bit of recon to pinpoint who they are. Oh, and it seems as though a lot of the guests are getting warmed up at the lounges before the conference begins. Best head over there.{/i}"

    Morgan "{i}Yes, I recognize a bunch of people on the guest list here, but nothing out of the ordinary so far. If I just...wait a minute!{/i}"

    Morgan "{i}That's him! That's Agent Graham! But what is he doing here?{/i}"

    Morgan "{i}Looks like Graham's making his move now, but he hasn't noticed me. The room he's trying to get into must have something to do with the assassination, but what do I do about all this?{/i}"

    menu:
        "Confront Agent Graham":
            jump sc_confrontation
        "Discreetly record Agent Graham":
            jump common_observation

    ""
    return




label sc_observation:
    
    ""
    return