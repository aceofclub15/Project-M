default     persistent.all_endings = False
default    persistent.assassin_ending = False
default    persistent.romance_ending = False
default    persistent.ace_ending = False
default    persistent.vigilante_ending = False



#SOUNDS SETTINGS
init python:


    print(renpy.music.channel_defined("background"))
    renpy.music.register_channel("background")
    

    def typing_sound(event, interact=True, **kwargs):
        if event == "show":  # When textbox is shown
            what = renpy.store._last_say_what # This grabs the text that was most recently spoken on-screen
            if what:
                sound_count = len(what)
            else:
                sound_count = 5

            for _ in range(sound_count): # This creates a sound queue based on how many characters are in the dialogue block
                randosound = renpy.random.randint(1,2) # This generates a random number between 1 and 11 inclusive. Change this based on how many sound files you have
                renpy.sound.queue(f"click{randosound}.wav", channel="sound", loop=False, relative_volume=1.5) # Change "popcat" to the name of your sound file

        elif event == "end" or event == "slow_done":
            renpy.sound.stop(channel="sound",fadeout=0.05) # This stops the text sounds if there is a pause in the dialogue or the text has finished displaying

            randosound = renpy.random.randint(1, 11) # This generates a random number between 1 and 11 inclusive. Change this based on how many sound files you have
            renpy.sound.play(f"click{randosound}.wav", channel="sound", loop=False, relative_volume=1.5) # This plays one final uninterrupted sound at the end of the dialogue block






default gender = ""
default romance = False

define Grandmaster = Character("Grandmaster", color="#e5ff00", callback=typing_sound)
define January = Character("January", color="#e5ff00", callback=typing_sound)

define Morgan = Character("Morgan", color="#00ffb7", callback=typing_sound)
define Young_Morgan = Character("Young Morgan", color="#6ec1a9")


define Sarah = Character("Sarah", color="#e94417")
define Graham = Character("Graham", color="#e0991c")
define June = Character("June Davidson", color="#9d00ff")
define Marcus = Character("Marcus Simms", color="#0e8b3c")


define Head_chef = Character("Head Chef",color="#fff")
define Crew_member = Character("Crew member", color="#0044ff")
define Agent_X = Character("Agent X", color = "#868686ff")
define Adam = Character("Adam (Target)", color="#ff2f00")
define Cop = Character("Police Officer", color ="#0044ff")
define Bartender = Character("Bartender", color="#ff419d")



label start:
    with Pause(0.5)
    jump sc_computer
    return



label sc_computer:
    scene black
    if (persistent.ace_ending) and (persistent.vigilante_ending) and (persistent.romance_ending) and (persistent.assassin_ending):
        $ persistent.all_endings = True
    $ renpy.music.queue("bg.wav",channel="background",loop=True, relative_volume=0.7)

    #Remember to add NVL mode to this part or something
    "Accessing personal info..."
    #"Please choose your character's gender (choice won't affect gameplay)"


    $gender = "Female"


    menu:
        "Accessing mission archives":
            jump sc_mission_archive

        "Login as Grandmaster (available after getting all endings)" if persistent.all_endings:
            jump sc_grandmaster_route_start
    return



label sc_mission_archive:
    scene black 
    show hologram_GM:
        xalign 0.5
        yalign 0.5
    
    Grandmaster "How are you feeling, Enforcer XIII?"
    Morgan "I'm feeling as ready as I'll ever be."
    Grandmaster "Good, because time is of the essence. The assassin from Davidson Solutions should've already infiltrated the hotel."
    Morgan "And I imagine the rogue Federal agent, Graham, is making his move too?"
    Grandmaster "Indeed, I have him on radar. It won't take long for him to arrive."
    Morgan "Are you sure you want to leave everything to me, Grandmaster?"
    Grandmaster "I am. This is your story, Morgan. I only need one thing from you."
    Morgan "That's right. I just need to make things interesting."
    Grandmaster "You catch on well."
    
    "The car slows to a stop."
    
    Morgan "Looks like we've arrived at the hotel. This is where I get out."
    Grandmaster "All the best, Morgan. I know you'll make me proud."
    Morgan "I aim to please, Grandmaster."
    
    jump sc_hotel_entrance
    return

label sc_hotel_entrance:
    show bg hotel_entrance
    show Morgan_default
    Morgan "{i}According to the Grandmaster\'s intel, Triplex CEO Adam Rourke will be attending the \'Future of the Extranet\' 
    conference in the 2nd Conference Hall, 90 minutes from now.{/i}"

    "90 minutes to assassination."

    Morgan "{i}Now, how should I take control of this situation?{/i}"

    menu:
        "Raise an alarm throughout the entire hotel":
            jump sc_emergency
        "Get hold of the guest list":
            jump sc_guest_list

    return


label sc_emergency:
    show bg emergency_room
    hide Morgan_default
    Morgan "Attention everyone! This is Officer Morgan of the FBI! I\'m declaring a terroristic threat at the Charleston! I need everyone to please-No wait, wait, don\'t escort me out, NOOOO!"
    scene black
    Grandmaster "You made a terrible judgment call, Morgan."
    Grandmaster "By attracting undue attention to yourself, you\'ve ensured that you\'ll be arrested and charged for impersonating a Federal officer."
    Grandmaster "As for Adam Rourke, he was assassinated, but the assassin did a sloppy enough job to get arrested as well."
    Grandmaster "An incredibly boring and anti-climactic way to end things."
    Grandmaster "I\'m disappointed."
    "GAME OVER"
    jump sc_hotel_entrance
    return

label sc_guest_list:
    Morgan "{i}That's right, I need to do this discreetly. If I get too many eyes on me, this mission's already a failure.{/i}"
    Morgan "Hi, excuse me! I'm Hendricks, from logistics. I just need to cross-check the guest list and make sure there are no empty tables at the 2nd Conference Hall. You know how the bosses are about wasted money."
    show Morgan_default at left with moveinright
    show Crew_member at right with moveinright
    Crew_member "Oh, I do, believe me. Here, take this flash drive. It should have everything you need to know about the Extranet conference."
    Morgan "Oh thank you, you're a lifesaver!"
    hide Crew_member with fade
    show Morgan_default at center with moveinleft
    Morgan "{i}Now, time to plug in the drive and see.{/i}"
    "A timer on the screen shows 60 minutes to assassination."
    Morgan "{i}It's as I suspected. This list has been tampered with. There's at least one person who isn't supposed to be here, but I'll need to do a bit of recon to pinpoint who they are.{/i}" 
    Morgan "{i}Oh, and it seems as though a lot of the guests are getting warmed up at the lounges before the conference begins. Best head over there.{/i}"
    "A timer on the screen shows 30 minutes to assassination."
    Morgan "{i}Yes, I recognize a bunch of people on the guest list here, but nothing out of the ordinary so far. If I just...wait a minute!{/i}"
    show Morgan_default at right with moveinleft
    show Graham at left with moveinleft
    "Graham stumbles out of a lounge, acting drunk."
    Morgan "{i}That's him! That's Agent Graham! But what is he doing here?{/i}"
    "He suddenly stops acting drunk. No one is watching him."
    "Graham approaches a locked door at the end of the hallway and pulls out a lockpick."
    Morgan "{i}Looks like Graham's making his move now, but he hasn't noticed me. The room he's trying to get into must have something to do with the assassination, but what do I do about all this?{/i}"
    
    menu:
        "Try to stop Graham by confronting him":
            jump sc_confrontation
        "Discreetly record Agent Graham":
            jump sc_observation

    return


label sc_observation:
    Morgan "Right, I have to be discreet. Can't go picking fights the first chance I get."
    Morgan " I'll just activate my thermoptic implant and set my video camera to record everything Graham does. Now, Graham, time for you to spill the beans."
    hide Morgan_default with fade
    show Graham at left
    "Graham lockpicks the door and barges in, confronting the man inside."
    show Agent_X:
        xalign 0.7
        yalign 0.9
        zoom 0.7
    Agent_X "Hey, who the hell are you? This room's closed!"
    Graham "Not anymore."
    hide Agent_X with fade
    show Graham at center with moveinleft
    "Graham fighting and punching out the man. Graham then hacks into the man's laptop" 
    "From the laptop a female voice can be heard."
    "Female voice" "{color=#ff0000} Mission update. I've infiltrated the conference room. Looking for a disguise now. Will finish the job soon. {/color}"

    show Graham:
        zoom 0.6
        xalign 0.8
        yalign 0.8
    with dissolve
    show Morgan_default at left with moveinleft
    Morgan "{i} Looks like the assassin's a woman, and she's pretty close to getting ready for the job. I need to make my way to the location ASAP! {/i}"
    Morgan "{i} But first, I need to hack Graham's phone to get more information. {/i}"
    Morgan "{i} The encryption on his phone's real strong, so I doubt I could trace it, but I can still call him if I decide to side with him. {/i}"
    Graham "Christ, why did it have to be her?! Well, I can't stop the assassination from here, but I WILL make"
    Graham "Sarah will pay for what she's done!"
    Morgan "{i}Those are some juicy details, but I really need to go now. I'm running out of time, and the moment of truth will soon be upon me. {/i}"
    "Morgan quickly go to the 2nd Conference room. The timer updates to show 10 minutes until the assassination. "
    Morgan "{i}If the killer is a woman, how can I narrow things down? How would an assassin infiltrate this place? {/i}"
    menu:
        "She might kill and replace someone":
            jump sc_sarah_kill
        "She might impersonate a staff member":
            jump sc_sarah_impersonate
    return





label sc_sarah_kill:
    scene black
    show bg hotel_entrance
    show Morgan_default at center
    Morgan "{i}She'll probably kill someone for the sake of a disguise. But who? Can I catch her in the act if I'm fast enough, or...?{/i}"
    "Morgan hears the sound of a thud, and someone struggling for their lives."
    Morgan "{i}Guess that answers my question. Time to go.{/i}"

    jump sc_sarah_attacking
    return

label sc_sarah_impersonate:
    scene black
    show bg hotel_entrance
    show Morgan_default at center
    Morgan "{i}She'll probably wear a disguise that gives her a lot of access, like a service staff member.{/i}"
    Morgan "{i}But where could she get such a disguise?{/i}"
    Morgan "{i}If she...{/i}"

    "Morgan hears a sound of someone struggling for their life."
    Morgan "{i}Shit, she's already making her move!{/i}"
    Morgan "{i}I need to act, now!{/i}"
    jump sc_sarah_attacking
    return

label sc_sarah_attacking:
    scene black
    show bg hotel_entrance
    "The assassin, Sarah, distically garroting a helpless female waiter to death and Morgan watches while hidden."
    show Staff:
        xalign 0.7
    with Pause(0.5)
    show Sarah:
        xalign 0.5
        zoom 1.3
    with moveinleft

    
    Sarah "You're not my target, darling, but you are quite the appetizer."
    show Staff:
        rotate 90
        xalign 0.8
        yoffset 400
        zoom 0.5

    Sarah "Regardless of how the mission goes, I still get to see the light go out of your eyes."
    Sarah "Thank you for that."

    "Morgan stays put as Sarah finishes her kill and drags the body away."

    Morgan "{i}So that's Sarah's disguise.{/i}"
    Morgan "{i}She's going to play as a waiter, probably deliver some poison straight into Rourke's thirsty mouth.{/i}"
    jump sc_chef_order
    return

label sc_chef_order:
    scene black
    show bg hotel_entrance with dissolve
    show Chef at left
    with Pause(0.5)
    show Sarah at right with moveinright
    Head_chef "Order up! We have a gin martini for Mr. Rourke, on the double!"
    "Sarah emerge in her waitress disguise as she takes Rourke's order and sneakily mixes something into the drink as Morgan notices."
    Sarah "Of course, ma'am. Right on it!"

    with Pause(0.5)
    hide Chef
    show Morgan_default at left with moveinleft
    Morgan "{i}This is it, the moment of truth.{/i}"
    Morgan "{i}The Grandmaster told me to make things interesting, but how am I going to do that now?{/i}"
    Morgan "{i}Whatever choice I make, there's no going back.{/i}"


    menu:
        "Help Sarah escape after she delivers the drink":
            jump sc_target_poisoned
        "Knock the drink out of Sarah's tray":
            jump sc_stop_sarah
        "Snatch up the drink and gulp it down":
            jump sc_drink_poison
    return







label sc_drink_poison:
    Morgan "Don't mind me!"

    Morgan "{i}Wait... what the hell was I thinking?{/i}"
    Morgan "{i}Now that I've swallowed this poisoned martini, it'll just... kill... me...{/i}"
    "Morgan downing the drink, and the screen immediately begins to blur."
    scene black with fade
    Grandmaster "Okay, that was kind of funny."
    Grandmaster "But seriously, you couldn't possibly have expected THAT choice to end well, right?"
    Grandmaster "...Right?"
    Grandmaster "Please start over before I think this over any further."
    "GAME OVER"
    jump sc_chef_order
    return


