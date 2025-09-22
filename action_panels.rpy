
label sc_timimg_shot:
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
