
label sc_timimg_shot:
    scene black with fade
    $ voice_line("m","oh","sur")
    Morgan "{i}Wait, I know how to pull this off.{/i}"
    Morgan "{i}To be a true assassin, you need mastery over time itself.{/i}"
    $ voice_line("m","hmm","bad")
    Morgan "{i}How about I bend the very laws of causality in my favor?{/i}"
    $ voice_line("m","so","ang")
    Morgan "{i}First, I'll shoot the metal plate on the left. Then the one on the right. After that, the one above.{/i}"
    $ voice_line("m","hmm","dis")
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
    $ voice_line("s", "yeah", "hap")
    Sarah "Wow, you actually did it."
    Sarah "This is amazing!"
    $ voice_line("m","good","dis")
    Morgan "Now am I good enough for you?"
    "Sarah blushes"
    $ voice_line("s","well","hap")
    Sarah "You are... if you want to be, that is."

    $ voice_line("m","hmm","bad")
    Morgan "{i}That's quite the invitation in her eyes.{/i}"
    Morgan "{i}But is this the kind of story I've been aspiring to?{/i}"
    $ voice_line("m","hmm","dis")
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
    $ voice_line("m","oh","sur")
    Morgan "Oops! Excuse me..."
    show ap_spilled_drink_1
    "Morgan {i} accidentally {/i} knocks the poisoned gin martini off the tray, causing the drink to spill onto the floor."
    pause 0.5
    show ap_spilled_drink_2
    pause 1.0
    "Morgan discreetly slips a tracker on Sarah, who looks furious about the accident before she composes herself."
    $ voice_line("m","whoa","hap")
    Morgan "Oh my god! I'm so sorry! I didn't..."
    $ voice_line("s","hmmph","ang")
    Sarah "Hmph. No problem at all, sir. Excuse me."
    "Sarah leaves the scene and Morgan also hurrily does so"
    
    scene black 
    show bg hotel
    $ voice_line("m","right","hap")
    Morgan "{i}Right, I need to take advantage of this window and call Graham immediately!{/i}"
    "Morgan dials a number."
    
    $ voice_line("g", "huh", "sur")
    Graham "Huh? Who is this? How did you get this number?"
    $ voice_line("m","so","bad")
    Morgan "I'm someone trying to stop an assassination, and I think you know which one I'm talking about."
    $ voice_line("m","hmm","dis")
    Morgan "I've delayed your dear friend Sarah, but time is short. I need your help."

    
    $ voice_line("g", "wait", "dis")
    Graham "Did you say Sarah?"
    
    $ voice_line("m","yeah","sad")
    Morgan "Yes. I recorded you infiltrating the lounge and knocking out Sarah's handler."
    $ voice_line("m","so","bad")
    Morgan "I know you have a personal vendetta against her. Work with me, and we can stop her."
    
    Morgan "{i}Time to show him the recording.{/i}"
    "Morgan wirelessly sends the lounge recording to Graham, who's in another room. We see Graham's eyes widen in shock as he watches it."
    
    $ voice_line("g","damn","hap")
    Graham "Damn, so you really were there."
    $ voice_line("g", "well", "bad")
    Graham "I was planning to go after Sarah after she went through with her little murder plan, but if you're here to save Adam's life, that'd be a big weight off my conscience."
    
    $ voice_line("m","well","hap")
    Morgan "I need you to be my eyes and ears. I'm taking Adam to safety, but Sarah will come after us soon. I've also just planted a tracker on her"
    
    "Morgan wirelessly transmits the tracker details."
    $ voice_line("g", "yeah", "sad")
    Graham "Yes, I have it. I see that Sarah's gone into the storage room."
    Graham "Whatever she plans to do next, it can't be good. You need to get out of here, quickly!"
    $ voice_line("m","yes","hap")
    Morgan "Understood, Graham."
    jump sc_approach_adam





label sc_romance_climax:

    $ voice_line("m","right","bad")
    Morgan "{i}My future with Sarah is all I care about now, and this asshole's in the way! He will die tonight!{/i}"

    $ voice_line("m","hmm","dis")
    Morgan "{i}Agent Graham may have cut through June's footsoldiers with ease, but they weren't masters of time like I am.{/i}"
    Morgan "{i}There's no move of his I can't foresee. No tactic of his I can't outmatch.{/i}"

    $ voice_line("m","hah","dis")
    Morgan "Time to die, Graham! This is for Sarah!"
    $ voice_line("s", "uh", "hap")
    Sarah "Goodbye, you sanctimonious old man. You won't be missed."
    window hide
    pause 0.75
    show ap_hq_fight_1
    pause 1
    show ap_hq_fight_2
    pause 1

    show ap_hq_fight_3
    pause 0.75
    show ap_hq_fight_4
    pause 1

    show ap_hq_fight_6
    pause 0.75
    show ap_hq_fight_7
    pause 1

    show ap_hq_fight_8
    pause 1
    show ap_hq_fight_9
    pause 1

    window show
    scene bg headquarters
    show Sarah at left
    show Graham at right
    show Morgan_default at right with moveinleft
    hide Graham with dissolve

    $ voice_line("m","yes","ang")
    Morgan "We did it... oh my God we did it, Sarah! We won!"
    $ voice_line("s","uh","hap")
    Sarah "That's right! We won, my love! The world is ours!"
    "They heard a voice from behind"
    $ voice_line("j","well","bad")
    "{color=#9d00ff} You two did win. A shame I can't say that for myself. {/color}"

    $ voice_line("s", "so", "ang")
    Sarah "Huh? What are you talking about, June? Graham's dead, we're in the clear."
    show June at left with moveinleft
    show Sarah at center with moveinleft

    $ voice_line("j","well","sad")
    June "It's the burdens of leadership, Sarah. I tried a gamble to get Graham out of hiding, and it let him straight to my headquarters."
    $ voice_line("j", "hmmph", "dis")
    June "You were just a pawn in my plans, so nobody will care what happens to you. But as for me? You'll find that my clients are rather... unforgiving."
    "Suddenly Morgan heard the sound of glass breaking and we see that June get shot through the head"

    show June:
        rotate 270
        yoffset 300
    with dissolve
    show Sarah at center with moveinright
    $ voice_line("s", "no", "ang")
    Sarah "What? No, June, NO!"
    $ voice_line("j", "ugh", "sad")
    June "Let this be a lesson to you both. If you play with fire... you're going to get burned."
    $ voice_line("j", "well", "bad")
    June "I made promises I couldn't keep, and this is the result..."

    $ voice_line("s", "no", "ang")
    Sarah "I'm sorry, June! I'm sorry I couldn't protect you! I promise I'll make it right!"
    $ voice_line("j","well","sad")
    June "(coughing) Don't repeat my mistakes, June... don't make a promise you can't keep..."
    June "I've used you for my ambitions all your life, sweet child... but now you need to live for yourself... Find a new life..."

    $ voice_line("m","yes","hap")
    Morgan "I'll protect her, June. I'll stay with her no matter what. You can rest easy now, okay?"
    $ voice_line("j","thanks","sad")
    June "Thank you, Morgan... please... make Sarah happy..."
    June "She deserves to be rewarded...for serving me so well... (cough)."
    $ voice_line("j", "oh", "fea")
    June "My precious January...I'm so sorry I can't be with you...even in this timeline..."

    $ voice_line("m","hmm","bad")
    Morgan "{i}It's heartbreaking to see Sarah's career culminate in such a tragedy. But perhaps things were always going to end this way.{/i}"
    $ voice_line("m","well","bad")
    Morgan "{i}At least she still got a chance to say goodbye. And she still has me to lean on.{/i}"
    Morgan "{i}I will protect her, no matter what. She won't meet the same end as her master.{/i}"
    $ voice_line("m","yeah","hap")
    Morgan "{i}We're both going to get our happy endings, no matter what it takes.{/i}"


   
    jump sc_romance_ending

    return


label sc_assassin_climax:

    Morgan "{i}I need to be careful with Graham. The Grandmaster might want to interrogate him and find out everything he knows.{/i}"

    $ voice_line("m","hmm","bad")
    Morgan "{i}I'll wear him down bit by bit. Sooner or later, he'll slip up... And I'll capture him!{/i}"


    Morgan "You're mine now, Graham. No sudden moves!"
    window hide
    pause 0.75
    show ap_hq_fight_1
    pause 1
    show ap_hq_fight_2
    pause 1

    show ap_hq_fight_3
    pause 0.75
    show ap_hq_fight_4
    pause 1
    

    scene bg headquarters
    show Graham at right
    with Pause(0.3)
    show Morgan_default at right with moveinleft
    show Sarah:
        xalign 0.2

    show Graham:
        rotate 90
        yoffset 300
        xoffset 200
    window show
    $ voice_line("g", "well", "hap")
    Graham "You really think you can take me alive? You think those two ladies will let you?!"

    $ voice_line("m","hah","dis")
    Morgan "You're not a threat anymore. Time to meet the Grandmaster, asshole."

    "There is a shout from behind"
    
    $ voice_line("j", "well", "bad")
    June "No, you can't!"

    $ voice_line("m","what","ang")
    Morgan "What are you doing, June? I'm on your side!"
    show June at left with moveinleft
    
    $ voice_line("j","grr","ang")
    June "If you're on my side, you'll hand over Graham, right now!"
    
    $ voice_line("m","huh","sur")
    Morgan "Huh? But why? I need to deliver her to my master!"
    
    $ voice_line("s", "so", "ang")
    Sarah "Do what June says, Morgan."
    "Sarah points the gun at Morgan"
    
    $ voice_line("m","tch","ang")
    Morgan "What the hell?! I can't just betray the Grandmaster-"

    $ voice_line("j", "god", "hap")
    June "You can't be serious, Morgan! You already know that she doesn't care what you do! Taking Graham to her's a waste of time, but if you hand him over to me, I can still fix-"

    # Sniper shot kills June
    "Suddenly Morgan heard the sound of glass breaking and we see that June get shot through the head"
    "June collapses"
    show June:   
        rotate 270
        yoffset 300
    with dissolve
    
    $ voice_line("s", "no", "ang")
    Sarah "June?! No! NOOO!"

    $ voice_line("g","so","bad")
    Graham "Looks like she was doomed from the very beginning, huh?"
    
    $ voice_line("m","what","sur")
    Morgan "Doomed? What are you talking about?"
    
    $ voice_line("g", "hah", "hap")
    Graham "Dear old June Davidson signed her own death warrant the moment I broke into this building."
    
    $ voice_line("g", "well", "hap")
    Graham "She's the one who went maverick and dragged me into this case to kill two birds with one stone, and look how that ended up for her."
    
    $ voice_line("s", "yeah", "ang")
    Sarah "Are you saying June brought this on herself?"
    
    $ voice_line("g","yeah","bad")
    Graham "Yup. She was only hired to kill Adam Roarke, nothing more. But she decided to get clever and use you for the job, knowing that it'd bring me out of hiding too."
    
    $ voice_line("g", "yes", "bad")
    Graham "Adam and I are both...connected, you see, and she thought she'd get a nice bonus by delivering both of our heads."
    Graham "Once everything went to shit, she probably wanted to capture me alive as a last-ditch Hail Mary. Well clearly, she was mistaken."
    
    $ voice_line("s","so","ang")
    Sarah "And that means I have no reason to keep you alive."
    "Sarah glares at Graham and shot him"
    with Pause(0.3)
    hide Graham with dissolve
    pause 0.3
    hide June
    # Sarah shoots Graham
    "A few moments later... Sarah still wears a sorrow look on her face"
    $ voice_line("m","hmm","sad")
    Morgan "{i}Seems like Graham did nothing to soften Sarah's pain. I could see she was still broken, that perhaps she always would be.{/i}"
    Morgan "{i}But still, we'd been through so much together. I didn't want things to end like this.{/i}"

    $ voice_line("m","well","bad")
    Morgan "Sarah..."

   
    $ voice_line("s", "so", "bad")
    Sarah "You need to leave, Morgan. Now."
    
    $ voice_line("m","sigh","sad")
    Morgan "But..."

    $ voice_line("s", "so", "bad")
    Sarah "I know this wasn't your fault. I know that. But I'm still angry, and I need to take it out on someone."
    Sarah "Please don't let it be you, Morgan. Go away, for your own sake."
    scene black

    $ voice_line("m","so","bad")
    Morgan "{i}And so I listen to her, and run.{/i}"
    Morgan "{i}My mission is over, and so is my partnership with Sarah.{/i}"
    $ voice_line("m","hmm","dis")
    Morgan "{i}It's time to go back to being an Enforcer, and wait for the Grandmaster's next orders.{/i}"
    "..."
    $ voice_line("m","so","bad")
    Morgan "{i}And so I continue working for Ouroboros.{/i}"

    jump sc_assassin_ending
    return
