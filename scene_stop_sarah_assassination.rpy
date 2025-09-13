label sc_stop_sarah:
    Morgan "{i}Looks like I'm playing the hero this time. In a manner of speaking, at least.{/i}"
    "Morgan walks up to Sarah."
    show Morgan_default at right with moveinleft
    Morgan "Oops! Excuse me..."
    "Morgan {i} accidentally {/i} knocks the poisoned Gin martini off the tray, causing the drink to spill onto the floor."
    "Morgan discreetly slips a tracker on Sarah, who looks furious about the accident before she composes herself."
    Morgan "Oh my god! I'm so sorry! I didn't..."
    Sarah "Hmph. No problem at all, sir. Excuse me."
    hide Sarah with dissolve
    hide Morgan_default with dissolve

    "Morgan also hurrily left the scene"
    "Change of scene."
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

    "scene changed."
    scene black
    show bg hotel_entrance
    show Adam at center
    "Morgan approaches Adam."
    Morgan "Excuse me, Mr. Adam Rourke, but I'm Agent Morgan from the FBI."
    Morgan "We've received credible intel that your life is in immediate danger, and you need to be secured."
    "Adam's bodyguard" "That's far enough. We need to see some ID and-"
    Adam "No. No we don't. I'll come with you, Agent Morgan. My life is in your hands."
    "Adam's bodyguard" "But sir!"
    Adam "You are relieved of duty. Thank you for your service."
    "Adam stands up and whispers in Morgan's ear."
    Adam "I know you're not FBI, but I also know I have no choice but to trust you. Get me out of this place, quickly!"
    Morgan "Of course. My master's prepared safe passage for you. Please come with me."
    "Morgan and Adam hurry out of the Charleston hotel, then rush to a getaway car prepared by Ouroboros."
    Morgan "Get in, quickly. You'll be taken somewhere safe."
    Adam "I see you're not coming with me. It's because of Graham, isn't it?"
    Morgan "You know about Graham?"
    Adam "I do, and I overheard you speaking to him through your earpiece. That's how I knew I could trust you."
    "Adam's expression hardens."
    Adam "Whoever it is that put a price on my head, you find them, and you destroy them. You hear me?!"
    Morgan "{i}Adam certainly seems used to throwing his weight around, with the way he's getting up in my face. But I don't have the time to put his ego in check, so I'll just go along to get along.{/i}"
    Morgan "Loud and clear, sir."
    Adam "Hmph."
    hide Adam with dissolve
    "Adam is driven away. The Grandmaster contacts Morgan through Morgan's wireless earpiece."
    Grandmaster "It looks like you're playing the hero this time around, huh, Morgan?"
    Morgan "That's right, Grandmaster. Is that okay with you?"
    Grandmaster "Of course it is. I asked you to make things interesting, and that's exactly what you're doing. Now rendezvous with Graham, and get to the bottom of this case."
    Morgan "Understood, ma'am."
    
    jump sc_meet_with_graham
    return



label sc_meet_with_graham:
    scene black
    show bg hotel_entrance
    "Time skips by 10 minutes as Morgan re-enters the hotel."
    "Graham calls Morgan's wireless earpiece."
    Graham "{i} I just got a message from this Ouroboros organization, telling me that Adam's been taken to safety.{/i}"
    Graham "{i}Your doing, I assume?{/i}"
    Morgan "That's right. What happened to Sarah?"
    Graham "{i}She's gone dark. I think she discovered the tracker you put on her.{/i}"
    Morgan "That's unfortunate. I guess we'll have to stay on guard and not leave the hotel."
    Graham "{i}Agreed. I'll book separate rooms for the two of us so that we can stay here for a couple of days.{/i}"
    Morgan "Good idea."
    Graham "{i}And...done. My room's 953 and yours is 966. We'll talk tomorrow.{/i}"
    "Graham disconnects. Morgan sits down at a bar, looking worn out."
    scene bar
    show Bartender at center
    Bartender "You look tired, ma'am. Is there anything I can do to help?"
    Morgan "{i}Wait, if Graham doesn't know where Sarah is, does that mean she's still around here, hunting us down?{/i}"
    Morgan "{i}The bartender seems overly assertive, but maybe it's just exhaustion's getting to me.{/i}"
    Bartender "I think you should retire to your room, sir. If you let me know the room number, I can call someone who's available, like miss Freida, to escort you."
    
    menu:
        "Sure, my room number's 966":
            jump sc_give_room_number
        "No thanks, I'm good":
            jump sc_keep_room_number
    return


label sc_give_room_number:
    Morgan "{i}Now that I get a closer look, she can't be Sarah. God, my paranoia's really getting to me. Still, I can't take any chances here. I'll just head up to my room alone.{/i}"
    Morgan "Yeah, my room number's 966. I don't mind an escort."
    Bartender "Certainly, ma'am. I'll call up someone immediately."
    "The female bartender dials up someone to escort Morgan. As soon as Morgan sees who's come for her, she's horrified."
    Morgan "{i}Shit, I screwed up! Sarah wasn't the bartender, but she's still infiltrated the service staff, and I let her right to me!{/i}"
    "Sarah, disguised as a staff member, quickly walks up to Morgan and tranquilizes them with a needle."
    Morgan "{i}Oh no, she's paralyzed me! I can't move!{/i}"
    Sarah "Relax, my dear. It'll all be over soon. We'll go over to your room, you'll tell me everything you know, and then I'll end it quickly. It's a pretty good way to die, all things considered."
    scene black
    Morgan "{i}I can't offer any resistance as Sarah carries me over to my room. She's right, I have no hope of making it out of this. Graham, Grandmaster, I'm so sorry...{/i}"
    Grandmaster "You can never be too careful in this line of work, Morgan. Sarah's like a chameleon, waiting to ambush you at the earliest opportunity. Don't give her any chance to track you down."
    "GAME OVER"
    
    jump sc_meet_with_graham
    return


label sc_keep_room_number:
    Morgan "{i}Now that I get a closer look, that can't be Sarah. {/i}"
    Morgan "{i}God, my paranoia's really getting to me. Still, I can't take any chances here. I'll just head up to my room alone.{/i}"
    "Morgan heads up to room 966, locks the door and puts a few security precautions in place before going to bed."
    
    
    "The scene cuts to the next day as Morgan's having breakfast in the hotel foyer."
    scene hotel_froyer
    "Graham contacts Morgan's wireless earpiece."
    Graham "{i}Feeling freshened up? Ready to discuss this case?{/i}"
    Morgan "Damn right I am. First things first, you need to tell me how you know Adam Rourke."
    Graham "{i}Adam and I go way back. We were both intelligence contractors for the CIA back during the days of the Afghan war.{/i}"
    Morgan "Is that why you showed up here? Because you knew Adam was the target?"
    Graham "{i}No, I showed up because of Sarah. She's...my sister-in-law.{/i}"
    Morgan "What?!"
    Graham "{i}Yeah, it's an ugly family secret. My wife, Jasmine, always thought Sarah was just independent and free-spirited.{/i}" 
    Graham "{i}Turns out she was a psychopathic serial killer the entire time. Jasmine and I only discovered this a few months into our marriage.{/i}" 
    Graham "{i}We tried to call the cops on Sarah, only for some hired goons to blow up our house.{/i}"
    Morgan "If reporting Sarah to the cops led to your house blowing up, that means Davidson Solutions must've already recruited her."
    Graham "{i}Davidson Solutions? You know about them too?{/i}"
    Morgan "Yeah, my master's done her own research on the matter."
    Graham "{i}Damn, those bastards must have an insane web of influence. I never thought I'd be dragged into their plans like this, though. {/i}"
    
    menu:
        "Yeah, I get you. This doesn't make any sense": 
            jump sc_nonsense
        "But they've planned this from the start":
            jump sc_they_planned_this #DOING THIS 
    return

label sc_they_planned_this:
    Morgan "I think Davidson Solutions hired Sarah for this job intentionally, to bring you out of hiding."
    Graham "{i}Bring me out of hiding? Wait a minute, could it be because...?{/i}"
    Morgan "Yes, it's probably your connection to Adam. Tell me, what did you two work on back in Afghanistan?"
    Graham "{i}Nothing much, just some deal that went bad. I wasn't even paid for it.{/i}"

    menu:
        "That's not much to go on":
            jump sc_no_lead
        "Oh, but you were paid":
            jump sc_graham_paid
    return






label sc_no_lead:
    Morgan "That's not much to go on. Looks like we've hit a dead end."
    Graham "{i}Yeah, this is super frustrating. I need to go outside, clear my head for a bit. Graham out.{/i}"
    "As Graham disconnects, Morgan leans back and ponders things."
    Morgan "{i}I really wish I'd done a better job of piecing things together, but in any case, our only option now is to hope for the best. {/i}"
    Morgan "{i}Maybe Graham might find something on his little soul-searching journey.{/i}"

    "Time skips by 10 minutes, when someone calls up Morgan's wireless earpiece."
    Morgan "Hello? Who is this?"
    "Female voice" "Your worst nightmare, Morgan. Would you kindly check your email? You'll find I've left a nice little present for you."
    "Morgan checks her email, and to her horror, she sees that a video's been sent showing Sarah standing over the body of a murdered Adam, and a captured Graham."
    Morgan "Oh, no!"
    "Female voice" "That's right, Enforcer XIII. You've failed to save Adam because he left your protection to go cover up his crimes."
    "Female voice" "I hold all the cards now. If you want Graham to live, you'll come to the Hallex warehouse in Queens. Alone."
    Morgan "{i}Did she just call me Enforcer XIII? How does she know about my job at Ouroboros? In any case, it's clear that I'm outmatched.{/i}"

    Morgan "{i}Seems like I have no choice then...{/i}"
    jump sc_obey_voice
    return




label sc_nonsense:
    Morgan "Yeah, I get you. This whole puzzle doesn't make any sense."
    Graham "{i}Just why the hell would Davidson Solutions want me dead? I need to go outside, take my mind off things."
    Morgan "Should I come with you?"
    Graham "{i}No, I need to think on this. Alone. Graham out."
    "As Graham disconnects, Morgan leans back and ponders things."
    Morgan "{i}I really wish I'd done a better job of piecing things together, but in any case, our only option now is to hope for the best and see if some other clues turn up. Maybe Graham might find something on his little soul-searching journey.{/i}"
    "Time skips by 10 minutes, when someone calls up Morgan's wireless earpiece."
    Morgan "Hello? Who is this?"
    "Female voice" "Your worst nightmare, Morgan. Would you kindly check your email? You'll find I've left a nice little present for you."
    "Morgan checks her email, and to her horror, she sees that a video's been sent showing Sarah standing over the body of a murdered Adam, and a captured Graham."
    Morgan "Oh, no!"
    "Female voice" "That's right, Enforcer XIII. You've failed to save Adam because he left your protection to go cover up his crimes. I hold all the cards now. If you want Graham to live, you'll come to the Hallex warehouse in Queens. Alone."
    Morgan "{i}Did she just call me Enforcer XIII? How does she know about my job at Ouroboros? In any case, it's clear that I'm outmatched.{/i}"
    
    menu:
        "I have no choice but to obey":
            jump sc_obey_voice
    return




