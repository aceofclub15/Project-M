default persistent.all_endings = False
default persistent.assassin_ending = False
default persistent.romance_ending = False
default persistent.ace_ending = False
default persistent.vigilante_ending = False
default persistent.first_time = 1
default list_endings = []

default history_focus = False
default dialogs_nav_focus = False
default save_focus = False
default pref_focus = False
default tree_focus = False
default tutorial_text=""



#TESTING STUFF: disable/delete if build for PUBLIC VER
define dev_build = True
define config.allow_skipping = dev_build
define config.fast_skipping = dev_build

default preferences.skip_unseen = dev_build




# AMOUNT OF ENDINGS CHECK!!!!!!
init python:
    def check_no_endings():
        list_endings = [persistent.assassin_ending, persistent.ace_ending, persistent.romance_ending, persistent.vigilante_ending]
        no_ends = 0
        for e in list_endings:
            if e == True:
                no_ends += 1
        return no_ends



#SOUNDS SETTINGS
init python:



    def ch_callbacks(event, **kwargs):
        typing_sound(event, **kwargs)
        name_callback(event, **kwargs)
    
    def typing_sound(event, interact=True, **kwargs):
        #TYPING SOUND WHEN TALKING !!!!!!!!!!!!!!!!!
        if event == "show":  
            what = renpy.store._last_say_what 
            if what:
                sound_count = len(what)
            else:
                sound_count = 5

            for _ in range(sound_count): 
                randosound = renpy.random.randint(1,2) 
                renpy.sound.queue(f"audio/sfx/click{randosound}.wav", channel="sound", loop=False, relative_volume=1.5) 

        elif event == "end" or event == "slow_done":
            renpy.sound.stop(channel="sound",fadeout=0.05) 



        








default gender = ""
default romance = False

define Grandmaster = Character("Grandmaster", color="#e5ff00", callback = name_callback, cb_name = "Grandmaster")
define January = Character("January", color="#e5ff00", callback = name_callback, cb_name = "January")

define Morgan = Character("Morgan", color="#00ffb7", callback = name_callback, cb_name = "Morgan")
define Young_Morgan = Character("Young Morgan", color="#6ec1a9", callback = name_callback, cb_name = "Morgan")


define Sarah = Character("Sarah", color="#e94417", callback = name_callback, cb_name = "Sarah")
define Graham = Character("Graham", color="#e0991c", callback = name_callback, cb_name = "Graham")
define June = Character("June Davidson", color="#9d00ff", callback = name_callback, cb_name = "June")
define Marcus = Character("Marcus Simms", color="#0e8b3c", callback = name_callback, cb_name = "Marcus")


define Head_chef = Character("Head Chef",color="#fff", callback = name_callback, cb_name = "Head_chef")
define Crew_member = Character("Crew member", color="#0044ff", callback = name_callback, cb_name = "Crew_member")
define Agent_X = Character("Agent X", color = "#868686ff", callback = name_callback, cb_name = "Agent_X")
define Adam = Character("Adam Rourke", color="#ff2f00", callback = name_callback, cb_name = "Adam")
define Cop = Character("Police Officer", color ="#0044ff", callback = name_callback, cb_name = "Cop")
define Bartender = Character("Bartender", color="#ff419d", callback = name_callback, cb_name = "Bartender")
define Bodyguard = Character("Bodyguard", color="#4525d5", callback = name_callback, cb_name = "Bodyguard")






default can_click_tree = True
screen button_tutorial_screen:
    tag menu
    zorder 99
    add Solid("#000")
    use quick_menu
    frame:
        xalign 0.5
        yalign 0.06
        background None
        has vbox
        text "Navigation Tutorial" xalign 0.5
    frame:
        xalign 0.5
        yalign 0.5
        background None
        text tutorial_text xalign 0.5


label button_tutorial:


    show screen button_tutorial_screen
    $ tutorial_text = "Welcome to the navigation tutorial! Here, you will learn how to use the quick menu to navigate around."
    ""

    $ history_focus = True
    $ tutorial_text = "Use the history button to open the text-log."
    ""
    

    $ save_focus = True
    $ history_focus = False
    $ tutorial_text = "These buttons let you Save or QuickSave your progress and Load your saves."
    ""

    # Step 3: preferences
    $ pref_focus = True
    $ save_focus = False
    $ tutorial_text = "The Preferences button opens game settings."
    ""


    $ dialogs_nav_focus = True
    $ pref_focus = False
    $ tutorial_text = "Back - go back one dialog \nSkip - skip through all dialogs until the next choice menu \nAuto - automatically go through the dialogs after a few seconds so you don't have to click."
    ""
    

    $ tree_focus = True
    $ dialogs_nav_focus = False
    $ tutorial_text = "Use the tree button to show your choices in the game."
    ""
    $ tree_focus = False
    

    $ tutorial_text = "For more key shortcuts, go to Preference to open the setting menu then Help"
    $ tutorial_text = "Enjoy the game!"
    ""


    hide screen button_tutorial_screen
    
    $ persistent.first_time = False
    stop music
    $ can_click_tree = True
    $ config.all_character_callbacks = [ch_callbacks]
    $ renpy.music.queue(music_bg_normal,channel="channel_background",loop=True)
    jump sc_computer
    return










init python:
    def render_node(node_id, depth=0, visited=None):
        if visited is None:
            visited = set()

        # Prevent re-rendering the same node
        if node_id in visited:
            return VBox()
        visited.add(node_id)

        node = persistent.story_tree[node_id]
        box = VBox()

        dis_text = ("   |" * depth) + ">" + node["name"]

        dis_color = node.get("color", "#ffffff")

        if node["unlocked"]:
            txt = renpy.text.text.Text(dis_text, size=22, color=dis_color)
            box.add(txt)

            # Recurse children
            for child in node["children"]:
                box.add(render_node(child, depth + 1, visited))

        return box





screen flowchart_screen():
    frame:
        vbox:
            spacing 8
            text "Progress Tree" size 30
            text "Color: " size 25
            text "-blue: important choice" color "#0099cc" size 25
            text "-green: common choice in many path" color "#66ff66" size 25
            text "-red: ending" color "#ff6666" size 25
            text "" size 25

            add render_node("start", 0)

    textbutton "Return" action Return() xalign 0.5 yalign 0.95







# GAME STORY START HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# GAME STORY START HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# GAME STORY START HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# GAME STORY START HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
label start:
    stop music
    $ can_click_tree = True
    $ config.all_character_callbacks = [ch_callbacks]
    $ renpy.music.queue(music_bg_normal,channel="channel_background",loop=True)
    jump sc_computer
    return



label sc_computer:
    scene black
    if (persistent.ace_ending) and (persistent.vigilante_ending) and (persistent.romance_ending) and (persistent.assassin_ending):
        $ persistent.all_endings = True

    #Remember to add NVL mode to this part or something
    "Accessing personal info... (choose who is logging in)"
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
    play sound sfx_tire_screech
    "The car slows to a stop."
    
    Morgan "Looks like we've arrived at the hotel. This is where I get out."



    Grandmaster "All the best, Morgan. I know you'll make me proud."
    Morgan "I aim to please, Grandmaster."
    
    jump sc_hotel_entrance
    return

label sc_hotel_entrance:
    show bg hotel
    show Morgan_default

    "Morgan saunters into the hotel like she's always belonged there. She is dressed in an elegant but understated business suit and has a suave smile with eyes betraying a sharp focus."
    Morgan "{i}According to the Grandmaster's intel, Hallex CEO Adam Rourke will be attending 'The Future of the Online Revolution and the Extranet' conference in the 2nd Conference Hall, 90 minutes from now.{/i}"
    "90 minutes to assassination."
    hide Morgan_default
    Morgan "{i}Now, how should I take control of this situation?{/i}"

    $ persistent.story_tree["start"]["unlocked"] = True

    menu:
        "Raise an alarm throughout the entire hotel":
            $ persistent.story_tree["emergency"]["unlocked"] = True
            jump sc_emergency
        "Get hold of the guest list":
            $ persistent.story_tree["discreet"]["unlocked"] = True
            jump sc_guest_list

    return


label sc_emergency:
    show bg emergency_room
    hide Morgan_default
    Morgan "Attention, everyone! This is Officer Morgan of the FBI! I\'m declaring a terroristic threat at the Charleston! I need everyone to please-No wait, wait, don\'t escort me out, NOOOO!"
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
            $ persistent.story_tree["stop_graham"]["unlocked"] = True
            jump sc_confrontation
        "Discreetly record Agent Graham":
            $ persistent.story_tree["record_graham"]["unlocked"] = True
            jump sc_observation

    return


label sc_observation:
    Morgan "Right, can't go picking fights the first chance I get."

    Morgan " I'll just activate my thermoptic implant and set my video camera to record everything Graham does. Now, Graham, it's time for you to spill the beans."
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
    Morgan "{i} Wow, I've picked up a lot of invaluable intel. It looks like the assassin's a woman. {/i}"
    Morgan "{i} She's pretty close to getting ready for the job, so I need to make my way to the location ASAP!{/i}"
    Morgan "{i}But first, let me just hack Graham's phone {/i}"
    Morgan "{i} The encryption on his phone is really strong, so I doubt I could trace it{/i}"
    Morgan "{i} But at least I can still call him if I decide to side with him. {/i}"
    
    Graham "Christ, why did it have to be her?! Well, I can't stop the assassination from here"
    Graham "But I'll make Sarah will pay for what she's done!"
    Morgan "{i}Those are some juicy details, but I really need to go now.The moment of truth will soon be upon me. {/i}"
    "Morgan quickly go to the 2nd Conference room. The timer updates to show 10 minutes until the assassination. "
    Morgan "{i}If the killer is a woman, how can I narrow things down? How would an assassin infiltrate this place? {/i}"
    menu:
        "She might kill and replace someone":
            $ persistent.story_tree["she_kill"]["unlocked"] = True
            jump sc_sarah_kill
        "She might impersonate a staff member":
            $ persistent.story_tree["she_impersonate"]["unlocked"] = True
            jump sc_sarah_impersonate
    return





label sc_sarah_kill:
    scene black
    show bg hotel
    show Morgan_default at center
    Morgan "{i}She'll probably kill someone for the sake of a disguise. But who? Can I catch her in the act if I'm fast enough, or...?{/i}"
    "Morgan hears the sound of a thud, and someone struggling for their lives."
    Morgan "{i}Guess that answers my question. Time to go.{/i}"

    jump sc_sarah_attacking
    return

label sc_sarah_impersonate:
    scene black
    show bg hotel
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
    $ persistent.story_tree["investigate"]["unlocked"] = True
    scene black
    show bg hotel
    "The assassin, Sarah, sadistically garroting a helpless female waiter to death and Morgan watches while hidden."
    show Staff:
        xalign 0.7
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
    show bg hotel_restaurant with dissolve
    #show Chef at left
    #with Pause(0.5)
    #show Sarah at right with moveinright
    Head_chef "Order up! We have a gin martini for Mr. Rourke, on the double!"
    "Sarah emerge in her waitress disguise as she takes Rourke's order and sneakily mixes something into the drink as Morgan notices."
    Sarah "Of course, ma'am. Right on it!"

    with Pause(0.5)
    hide Chef
    #show Morgan_default at left with moveinleft
    Morgan "{i}This is it, the moment of truth.{/i}"
    Morgan "{i}The Grandmaster told me to make things interesting, but how am I going to do that now?{/i}"
    Morgan "{i}Whatever choice I make, there's no going back.{/i}"


    menu:
        "Help Sarah escape after she delivers the drink":
            $ persistent.story_tree["help_sarah"]["unlocked"] = True
            jump sc_target_poisoned
        "Knock the drink out of Sarah's tray":
            $ persistent.story_tree["stop_sarah"]["unlocked"] = True
            jump sc_stop_sarah
        "Snatch up the drink and gulp it down":
            $ persistent.story_tree["drink_poison"]["unlocked"] = True
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


