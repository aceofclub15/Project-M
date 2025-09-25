
label sc_timimg_shot:
    scene black with fade
    Morgan "{i}Wait, I know how to pull this off.{/i}"
    Morgan "{i}To be a true assassin, you need mastery over time itself.{/i}"
    Morgan "{i}How about I bend the very laws of causality in my favor?{/i}"
    Morgan "{i}First, I'll shoot the metal plate on the left. Then the one on the right. After that, the one above.{/i}"
    Morgan "{i}If I get the angles right, I'll have triangulated my way to a bullseye.{/i}"
    window hide

    show ap_shooting_1
    pause 0.5
    show ap_shooting_2
    pause 0.5
    show ap_shooting_3
    pause 0.75
    show ap_shooting_4
    pause 0.75


    show ap_shooting_5
    python:
        for i in range(3):
            renpy.sound.queue(sfx_muffled_gun_shot)
            renpy.pause(0.25)
    pause 0.5
    scene black
    show bg shooting_range
    show Sarah at center with moveinbottom
    window show
    Sarah "Wow, you actually did it."
    Sarah "This is amazing!"
    Morgan "Now am I good enough for you?"
    "Sarah blushes"
    Sarah "You are... if you want to be, that is."

    Morgan "{i}That's quite the invitation in her eyes.{/i}"
    Morgan "{i}But is this the kind of story I've been aspiring to?{/i}"
    $ persistent.story_tree["choice4"]["unlocked"] = True
    menu:
        "Kiss her":
            $ persistent.story_tree["romance"]["unlocked"] = True
            jump sc_kiss_sarah
        "Keep it professional":
            $ persistent.story_tree["pro"]["unlocked"] = True
            jump sc_stay_professional
    return

label sc_stop_sarah:
    scene black
    show bg hotel_restaurant
    Morgan "{i}Looks like I'm playing the hero this time. In a manner of speaking, at least.{/i}"
    "Morgan walks up to Sarah."
    show Morgan_default at center with moveinbottom
    Morgan "Oops! Excuse me..."
    show ap_spilled_drink_1
    "Morgan {i} accidentally {/i} knocks the poisoned gin martini off the tray, causing the drink to spill onto the floor."
    pause 0.5
    show ap_spilled_drink_2
    pause 1.0
    "Morgan discreetly slips a tracker on Sarah, who looks furious about the accident before she composes herself."
    Morgan "Oh my god! I'm so sorry! I didn't..."
    Sarah "Hmph. No problem at all, sir. Excuse me."
    "Sarah leaves the scene and Morgan also hurrily does so"
    scene black 
    show bg hotel
    Morgan "{i}Right, I need to take advantage of this window and call Graham immediately!{/i}"
    "Morgan dials a number."
    Graham "Huh? Who is this? How did you get this number?"
    Morgan "I'm someone trying to stop an assassination, and I think you know which one I'm talking about. I've delayed your dear friend Sarah, but time is short. I need your help."
    Graham "Did you say Sarah?"
    Morgan "Yes. I recorded you infiltrating the lounge and knocking out Sarah's handler. I know you have a personal vendetta against her. Work with me, and we can stop her."
    Morgan "{i}Time to show him the recording.{/i}"
    "Morgan wirelessly sends the lounge recording to Graham, who's in another room. We see Graham's eyes widen in shock as he watches it."
    Graham "Damn, so you really were there."
    Graham "I was planning to go after Sarah after she went through with her little murder plan, but if you're here to save Adam's life, that'd be a big weight off my conscience."
    Morgan "I need you to be my eyes and ears. I'm taking Adam to safety, but Sarah will come after us soon."
    Morgan "I've also just planted a tracker on her"
    "Morgan wirelessly transmits the tracker details."
    Graham "Yes, I have it. I see that Sarah's gone into the storage room."
    Graham "Whatever she plans to do next, it can't be good. You need to get out of here, quickly!"
    Morgan "Understood, Graham."
    jump sc_approach_adam