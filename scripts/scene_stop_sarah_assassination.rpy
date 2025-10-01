###THE SCENE BEFORE IS IN AP


###THE SCENE BEFORE IS IN AP
label sc_approach_adam:
    scene black
    show bg hotel

    show Adam at right

    "Morgan approaches Adam."
    show Morgan_default at left with moveinleft
    $ voice_line("m","well","hap")
    Morgan "Excuse me, Mr. Adam Rourke, but I'm Agent Morgan from the FBI."
    Morgan "We've received credible intel that your life is in immediate danger, and you need to be secured."
    show Bodyguard:
        align (0.6, 0.8)

    Bodyguard "That's far enough. We need to see some ID and-"
    $ voice_line("a", "no", "ang")
    Adam "No. No we don't. I'll come with you, Agent Morgan. My life is in your hands."

    Bodyguard "But sir!"
    $ voice_line("a", "hmm", "sur")
    Adam "You are relieved of duty. Thank you for your service."

    hide Bodyguard with dissolve
    "Adam whispers in Morgan's ear."
    $ voice_line("a","haha","bad")
    Adam "I know you're not FBI, but I also know I have no choice but to trust you."
    $ voice_line("a", "hmm", "sur")
    Adam "Get me out of this place, quickly!"
    $ voice_line("m","yeah","sad")
    Morgan "Of course. My master's prepared safe passage for you. Please come with me."

    "Morgan and Adam hurry out of the Charleston hotel, rushing to a getaway car prepared by Ouroboros."
    Morgan "Get in, quickly. You'll be taken somewhere safe."
    $ voice_line("a", "hmm", "bad")
    Adam "I see you're not coming with me. It's because of Graham, isn't it?"

    $ voice_line("m","huh","sur")
    Morgan "You know about Graham?"
    $ voice_line("a","haha","bad")
    Adam "I do, and I overheard you speaking to him through your earpiece. That's how I knew I could trust you."

    $ voice_line("a","grr","ang")
    Adam "(gritting teeth) Whoever it is that put a price on my head, you find them, and you destroy them. You hear me?!"
    Morgan "{i}Adam certainly seems used to throwing his weight around, with the way he's getting up in my face. But I don't have the time to put his ego in check, so I'll just go along to get along.{/i}"
    $ voice_line("m","yes","hap")
    Morgan "Loud and clear, sir."
    $ voice_line("a", "hmm", "ang")
    Adam "Hmph."
    hide Adam with dissolve
    play sound sfx_car_leaving volume 1.5 fadeout 0.5
    pause 1
    "Adam is driven away. The Grandmaster contacts Morgan through her earpiece."
    $ voice_line("gm","hmmph","bad")
    Grandmaster "It looks like you're playing the hero this time around, huh, Morgan?"
    $ voice_line("m","yes","ang")
    Morgan "That's right, Grandmaster. Is that okay with you?"
    $ voice_line("gm","yes","ang")
    Grandmaster "Of course it is. I asked you to make things interesting, and that's exactly what you're doing."
    $ voice_line("gm","okay","hap")
    Grandmaster "Now rendezvous with Graham, and get to the bottom of this case."
    $ voice_line("m","right","hap")
    Morgan "Understood, ma'am."

    jump sc_meet_with_graham
    return


label sc_meet_with_graham:
    scene black
    show bg hotel
    "Ten minutes later, Graham calls Morgan at the hotel."
    show Morgan_default at center with dissolve
    $ voice_line("g","well","bad")
    Graham "I just got a message from this Ouroboros organization, telling me that Adam's been taken to safety. Your doing, I assume?"
    $ voice_line("m","right","bad")
    Morgan "That's right. What happened to Sarah?"
    $ voice_line("g", "tch", "bad")
    Graham "She's gone dark. I think she discovered the tracker you put on her."
    $ voice_line("m","sigh","bad")
    Morgan "That's unfortunate. I guess we'll have to stay on guard and not leave the hotel."
    $ voice_line("g","yes","bad")
    Graham "Agreed. I'll book separate rooms for the two of us so that we can stay here for a couple of days."
    $ voice_line("m","good","hap")
    Morgan "Good idea!"
    $ voice_line("g","well","bad")
    Graham "Done. My room's 953 and yours is 966. We'll talk tomorrow."
    "Graham disconnects. Morgan sits down at a bar, worn out."
    #scene hotel with dissolve
    show Morgan_default at left with moveinright
    show Bartender at right
    Bartender "You look tired, ma'am. Is there anything I can do to help?"
    $ voice_line("m","hmm","bad")
    Morgan "{i}Wait, if Graham doesn't know where Sarah is, does that mean she's still around here, hunting us down?{/i}"
    $ voice_line("m","uh","bad")
    Morgan "{i}The bartender seems overly assertive, but maybe it's just exhaustion's getting to me.{/i}"
    Bartender "I think you should retire to your room, ma'am. If you let me know the room number, I can call someone who's available, like Miss Freida, to escort you."
    menu:
        "Sure, my room number's 966":
            $ persistent.story_tree["give_room"]["unlocked"] = True
            jump sc_give_room_number
        "No thanks, I'm good":
            $ persistent.story_tree["dont_give_room"]["unlocked"] = True
            jump sc_keep_room_number
    return


label sc_give_room_number:
    $ voice_line("m","no","sad")
    Morgan "{i}No, now that I get a closer look, she can't be Sarah. I guess I can trust her a little.{/i}"
    $ voice_line("m","thanks","sad")
    Morgan "Thanks, my room number's 966. I don't mind an escort."
    Bartender "Certainly, ma'am. I'll call up someone immediately."
    "The female bartender calls Freida to escort Morgan. As soon as Morgan sees Freida, she's horrified."
    hide Bartender with dissolve
    show Sarah_disguise at right with moveinright
    $ voice_line("m","shit","dis")
    Morgan "{i}Shit, I screwed up! I did not think that she'll be here, and now I've led her right to me!{/i}"
    "Sarah quickly dashes to Morgan and put a needle in her arm."
    show Sarah_disguise at left with moveinright
    show Morgan_default:
        xalign 0.1
        yalign 0.85
    $ voice_line("m", "oh", "sur")
    Morgan "{i}Oh no, she's paralyzed me! I can't move!{/i}"
    $ voice_line("s", "uh", "hap")
    Sarah "Relax, my dear. It'll all be over soon. We'll go to your room, you'll tell me everything you know, and then I'll end it quickly."
    Sarah "It's a pretty good way to die, all things considered."
    scene black
    Morgan "{i}I can't offer any resistance as Sarah carries me over to my room. She's right, I have no hope of making it out of this. Graham, Grandmaster, I'm so sorry...{/i}"
    $ voice_line("gm","well","sad")
    Grandmaster "You can never be too careful in this line of work, Morgan. Sarah's like a chameleon, waiting to ambush you at the earliest opportunity. Don't give her any chance to track you down."
    "GAME OVER"
    
    jump sc_meet_with_graham
    return


label sc_keep_room_number:
    $ voice_line("m","no","sad")
    Morgan "No, but thank you anyway!"
    Morgan "{i}Now that I get a closer look, that can't be Sarah. {/i}"
    $ voice_line("m","sigh","hap")
    Morgan "{i}God, my paranoia's really getting to me. Still, I can't take any chances here. I'll just head up to my room alone.{/i}"
    "Morgan heads up to her room, locks the door and goes to bed."
    
    scene black
    scene hotel #hotel_foyer
    "The next morning, Graham contacts Morgan while she is having breakfast."
    show Morgan_default at left 
    show Graham at right
    $ voice_line("g", "well", "hap")
    Graham "Feeling freshened up? Ready to discuss this case?"
    $ voice_line("m","yes","ang")
    Morgan "Damn right I am. First things first, you need to tell me how you know Adam Rourke."
    $ voice_line("g","well","bad")
    Graham "Adam and I go way back. We were both intelligence contractors for the CIA back during the days of the Afghan war."
    $ voice_line("m","huh","sur")
    Morgan "Is that why you showed up here? Because you knew Adam was the target?"
    $ voice_line("g", "sigh", "sad")
    Graham "No, I showed up because of Sarah. She's...my sister-in-law."
    $ voice_line("m","what","sur")
    Morgan "What?!"
    $ voice_line("g", "yeah", "sad")
    Graham "Yeah, it's an ugly family secret. My wife, Jasmine, always thought Sarah was just independent and free-spirited." 
    $ voice_line("g","what","sur")
    Graham "Turns out she was a psychopathic serial killer the entire time. Jasmine and I only discovered this a few months into our marriage." 
    $ voice_line("g", "well", "bad")
    Graham "We tried to call the cops on Sarah, only for some hired goons to blow up our house."
    $ voice_line("m","hmm","sad")
    Morgan "If reporting Sarah to the cops led to your house blowing up, that means Davidson Solutions must have already recruited her."
    $ voice_line("g", "what", "fea")
    Graham "Davidson Solutions? You know about them too?"
    $ voice_line("m","yes","hap")
    Morgan "Yeah, my master's done her own research on the matter."
    $ voice_line("g", "damn", "hap")
    Graham "Damn, those bastards must have an insane web of influence. I never thought I'd be dragged into their plans like this, though."
    $ persistent.story_tree["choice3"]["unlocked"] = True
    menu:
        "Yeah, I get you. This doesn't make any sense": 
            $ persistent.story_tree["no_sense"]["unlocked"] = True
            jump sc_nonsense
        "But they've planned this from the start":
            $ persistent.story_tree["planned"]["unlocked"] = True
            jump sc_they_planned_this 
    return

label sc_they_planned_this:
    $ voice_line("m","well","bad")
    Morgan "I think Davidson Solutions hired Sarah for this job intentionally, to bring you out of hiding."
    $ voice_line("g", "wait", "dis")
    Graham "Bring me out of hiding? Wait a minute, could it be because...?"
    $ voice_line("m","yeah","sad")
    Morgan "Yes, it's probably your connection to Adam. Tell me, what did you two work on back in Afghanistan?"
    $ voice_line("g", "well", "bad")
    Graham "Nothing much, just some deal that went bad. I wasn't even paid for it."

    $ voice_line("m","hmm","sad")
    menu:
        "That's not much to go on":
            $ persistent.story_tree["no_sense"]["unlocked"] = True
            jump sc_no_lead
        "Oh, but you were paid":
            jump sc_graham_paid
    return


label sc_no_lead:
    $ voice_line("m","hmm","sad")
    Morgan "That's not much to go on. Looks like we've hit a dead end."
    $ voice_line("g", "sigh", "sad")
    Graham "Yeah, this is super frustrating. I need to go outside, clear my head for a bit. Graham out."
    "As Graham leaves, Morgan leans back and ponders things."
    hide Graham with dissolve 
    show Morgan_default at center with moveinleft
    $ voice_line("m","sigh","hap")
    Morgan "{i}I really wish I'd done a better job of piecing things together, but in any case, our only option now is to hope for the best. {/i}"
    Morgan "{i}Maybe Graham might find something on his little soul-searching journey.{/i}"

    "Time skips by 10 minutes, when someone calls up Morgan's wireless earpiece."
    $ voice_line("m","huh","sur")
    Morgan "Hello? Who is this?"
    $ voice_line("j","well","hap")
    "Female voice" "{color=#9d00ff} Your worst nightmare, Morgan. Would you kindly check your email? You'll find I've left a nice little present for you. {/color}"
    "Morgan checks her email, and to her horror, she sees that a video's been sent showing Sarah standing over the body of a murdered Adam, and a captured Graham."
    $ voice_line("m","shit","dis")
    Morgan "Shit."
    "Female voice" "{color=#9d00ff} That's right, Enforcer XIII. You've failed to save Adam because he left your protection to go cover up his crimes. {/color}"
    "Female voice" "{color=#9d00ff} I hold all the cards now. If you want Graham to live, you'll come to the Hallex warehouse in Queens. Alone. {/color}"
    $ voice_line("m","oh","sur")
    Morgan "{i}Did she just call me Enforcer XIII? How does she know about my job at Ouroboros? In any case, it's clear that I'm outmatched.{/i}"

    $ voice_line("m","well","bad")
    Morgan "{i}Seems like I have no choice then...{/i}"
    jump sc_obey_voice
    return


label sc_nonsense:
    $ voice_line("m","yeah","sad")
    Morgan "Yeah, I get you. This whole puzzle doesn't make any sense."
    $ voice_line("g","well","bad")
    Graham "Just why the hell would Davidson Solutions want me dead? I need to go outside, take my mind off things."
    $ voice_line("m","well","bad")
    Morgan "Should I come with you?"
    $ voice_line("g","no","bad")
    Graham "No, I need to think on this. Alone."
    hide Graham with dissolve 
    show Morgan_default at center with moveinleft
    "As Graham leaves, Morgan leans back and ponders things."
    $ voice_line("m","sigh","hap")
    Morgan "{i}I really wish I'd done a better job of piecing things together, but in any case, our only option now is to wait and see if some other clues turn up. {/i}"
    $ voice_line("m","well","bad")
    Morgan "{i}Well, maybe Graham might find something on his little soul-searching journey.{/i}"
    "10 minutes later, Morgan recieves an anonymous call."
    $ voice_line("m","huh","sur")
    Morgan "Hello? Who is this?"
    $ voice_line("j","well","hap")
    "Female voice" "{color=#9d00ff} Your worst nightmare, Enforcer XIII. Would you kindly check your email? You'll find I've left a nice little present for you. {/color}"
    "Morgan checks her email. The unknown caller sent multiple pictures showing a dead Adam, and a captured Graham."
    $ voice_line("m","shit","dis")
    Morgan "Shit."
    $ voice_line("j","right","hap")
    "Female voice" "{color=#9d00ff} That's right, Enforcer XIII. You've failed to save Adam because he left your protection to go cover up his crimes. I hold all the cards now. If you want Graham to live, you'll come to the Hallex warehouse in Queens. Alone. {/color}"
    $ voice_line("m","oh","sur")
    Morgan "{i}Did she just call me Enforcer XIII? How does she know about my job at Ouroboros? In any case, it's clear that I'm outmatched.{/i}"
    
    $ voice_line("m","well","bad")
    menu:
        "I have no choice but to obey":
            jump sc_obey_voice
    return