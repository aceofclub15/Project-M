default gender = ""
default romance = False

define Grandmaster = Character("Grandmaster", color="#e5ff00")
define Morgan = Character("Morgan", color="#00ffb7")
define Young_Morgan = Character("Young Morgan", color="#6ec1a9")


define Sarah = Character("Sarah", color="#e94417")
define Graham = Character("Graham", color="#e0991c")
define June = Character("June Davidson", color="#9d00ff")


define Head_chef = Character("Head Chef",color="#fff")
define Crew_member = Character("Crew member", color="#0044ff")
define Agent = Character("Agent X", color = "#868686ff")
define Adam = Character("Adam (Target)", color="#ff2f00")
define Cop = Character("Police Officer", color ="#0044ff")


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
    hide Morgan_default
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

    Crew_member "Oh, I do, believe me. Here, take this flash drive. It should have everything you need to know about the Extranet conference."

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
            jump sc_observation

    ""
    return




label sc_observation:
    Morgan "Right, I have to be discreet. Can't go picking fights the first chance I get."
    Morgan "I'll just activate my thermoptic implant and set the DataReader to record. Now, Graham, time for you to spill the beans."
    Agent "Hey, who the hell are you? This room's closed!"
    Graham "Not anymore."
    "{color=#ff0000} I've infiltrated the conference room. Looking for a disguise now. {/color}"
    Morgan "{i} Looks like the assassin's a woman, and she's pretty close to getting ready for the job. I need to make my way to the location ASAP! {/i}"
    Morgan "{i} But first, let me just hack Graham's phone. {/i}"
    Morgan "{i} The encryption on his phone's real strong, so I doubt I could trace it, but I can still call him if I decide to side with him. {/i}"
    Graham "Christ, why did it have to be her?! Well, I can't stop the assassination from here, but I WILL make"
    Graham "Sarah will pay for what she's done!"
    Morgan "Those are some juicy details, but I really need to go now. I'm running out of time, and the moment of truth will soon be upon me."
    Morgan "If the killer is a woman, how can I narrow things down? How would an assassin infiltrate this place?"
    menu:
        "She might kill and replace someone":
            jump sc_sarah_kill
        "She might impersonate a staff member":
            jump sc_sarah_impersonate
    return


label sc_sarah_kill:
    Morgan "{i}She'll probably kill someone for the sake of a disguise.{/i}"
    Morgan "{i}But who?{/i}"
    Morgan "{i}Can I catch her in the act if I'm fast enough, or...?{/i}"

    Morgan "{i}Guess that answers my question.{/i}"
    Morgan "{i}Time to go.{/i}"

    jump sc_sarah_attacking
    return

label sc_sarah_impersonate:
    Morgan "{i}She'll probably wear a disguise that gives her a lot of access, like a service staff member.{/i}"
    Morgan "{i}But where could she get such a disguise?{/i}"
    Morgan "{i}If she...{/i}"

    Morgan "{i}Shit, she's already making her move!{/i}"
    Morgan "{i}I need to act, now!{/i}"
    jump sc_sarah_attacking
    return

label sc_sarah_attacking:
    Sarah "You're not my target, darling, but you are quite the appetizer."
    Sarah "Regardless of how the mission goes, I still get to see the light go out of your eyes."
    Sarah "Thank you for that."

    Morgan "{i}So that's Sarah's disguise.{/i}"
    Morgan "{i}She's going to play as a waiter, probably deliver some poison straight into Rourke's thirsty mouth.{/i}"

    Head_chef "Order up! We have a gin martini for Mr. Roarke, on the double!"

    Sarah "Of course, ma'am. Right on it!"

    Morgan "{i}This is it, moment of truth.{/i}"
    Morgan "{i}The Grandmaster told me to make things interesting, but how am I going to do that now?{/i}"
    Morgan "{i}Whatever choice I make, there's no going back.{/i}"

    menu:
        "Approach Sarah after she delivers the drink":
            jump sc_target_poisoned
        "Knock the drink out of Sarah's tray":
            "jump Detective_route_1"
            return
        "Snatch up the drink and gulp it down":
            jump sc_drink_poison
    return


label sc_drink_poison:
    Morgan "Don't mind me!"

    Morgan "{i}Wait... what the hell was I thinking?{/i}"
    Morgan "{i}Now that I've swallowed this poisoned martini, it'll just... kill... me...{/i}"

    Grandmaster "Okay, that was kind of funny."
    Grandmaster "But seriously, you couldn't possibly have expected THAT choice to end well, right?"
    Grandmaster "...Right?"
    Grandmaster "Please start over before I think this over any further."

    jump sc_sarah_attacking
    return


