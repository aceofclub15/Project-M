label sc_target_poisoned:
    Morgan "{i}Looks like I'm siding with the psychopathic murderer.{/i}"
    Morgan "{i}And I can't deny there's a certain thrill to being a villain here.{/i}"
    Morgan "{i}Alright, Sarah, show me what you've got.{/i}"

    scene black
    show bg hotel_entrance
    show Adam:
        xalign 0.7
    with moveinbottom
    with Pause(0.2)
    show Sarah:
        xalign 0.5
        zoom 1.3
    with moveinleft

    Sarah "Your order, sir."
    Adam "Yes, thanks."

    "Some montage of Adam gulping down the drink and Sarah gracefully left the dining area"
    "..."
    scene black
    show bg hotel_entrance

    "As Sarah leaves Rourke's table, Morgan approaches her."
    show Sarah:
        xalign 0.7
    with moveinbottom
    with Pause(0.2)
    show Morgan_default:
        xalign 0.5
        zoom 1.3
    with moveinleft
    Morgan "Evening ma'am, mind if I have a word?"

    Sarah "I'm sorry, can I help you with something?"
    "Morgan leans into Sarah's ear."
    Morgan "Listen carefully and keep cool."
    Morgan "You're being followed."
    Morgan "Someone's come here to apprehend you."
    
    "Sarah's voice hardens."
    Sarah "What? How do you know this?!"

    Morgan "Does the name Graham ring a bell?  I have a recording of him knocking out your handler at the lounge."

    Sarah "Shit, if he's the one who found me, I'm in serious trouble."
    Sarah "I don't exactly trust you right now, but I can't risk ignoring this."
    Sarah "Do you have anything else for me?"

    Morgan "Indeed. I have an alternate extraction route, prepped and ready at the behest of my master."
    Morgan "That should throw Graham off your trail, and we can rendezvous sometime later."

    "Rourke convulses under the effect of the poison as he's hastily ushered out."
    Morgan "Looks like things are escalating. What's your decision, Sarah?"
    Morgan "What's your decision, Sarah?"

    Sarah "Fine. Give me the coordinates, quickly."

    "Morgan beams the new extraction coordinates."
    Sarah "I got them. I hope I can trust you."
    Morgan "Now go, quickly!"
    
    with Pause(0.5)
    scene black 
    "Sarah and Morgan part ways. After that, the Grandmaster calls Morgan."
    show hologram_GM:
        xalign 0.5
        yalign 0.5
    Grandmaster "So you've chosen to aid and abet a murderer, have you?"
    Grandmaster "Well, I just wanted to let you know that Adam's death has been confirmed and Sarah's arrived at the exfil point, safe and sound."
    Grandmaster "I've also given her your contact information and told her to contact you tomorrow."
    Grandmaster "Time for you to see this through the end."

    Morgan "Thank you, Grandmaster. I promise I won't disappoint."

    Grandmaster "I know you won't, Morgan. Until next time."

    Morgan "{i}I've made my decision, now it's time to see where it takes me.{/i}"
    Morgan "{i}I'm looking forward to hearing from Sarah again.{/i}"

    jump sc_next_day
    return



label sc_next_day:
    scene metting area
    "..."
    "Some time have passed"
    show Morgan_default at center with moveinleft
    
    Morgan "{i}I received a message from Sarah, telling me to meet her, alone, at a deserted shooting range.{/i}"
    Morgan "{i}Being asked to come alone is already a red flag, but I did willingly choose the path of danger, after all.{/i}"
    "Morgan gets into a car and drives to the shooting range."
    "Morgan arrived and wait for a few moments"
    Morgan "Hello, Sarah. Looks like you made it out of the last job safely."
    show Sarah at right with moveinright
    Sarah "I did. You were true to your word."
    Sarah "I still don't know why you helped me, though."

    Morgan "The answer to that is simple."
    Morgan "Because I wanted to."

    Sarah "And your master just lets you go around doing whatever you want?"

    Morgan "In a manner of speaking."

    Sarah "You've just made yourself an accomplice to a high-profile murder."
    Sarah "You do seem to have the stomach for my line of work, but whether you have the skill is another question entirely."

    Sarah "Show me you have what it takes, Morgan, and we can do great things together."

    Morgan "I already helped you get away with murder, isn't that good enough for you?"

    Sarah "I decide what's good enough for me."
    Sarah "Now are you going to hit the target or not?"

    Morgan "{i}The challenge she's set up is ridiculous.{/i}"
    Morgan "{i}Like that 'curve the bullet' scene from the Wanted movie.{/i}"
    Morgan "{i}How the hell am I supposed to pull this off?{/i}"

    menu:
        "Guess I'll just open fire and hope for the best":
            jump sc_random_shot
        "Maybe the key is to overpower time itself":
            jump sc_timimg_shot
    return


label sc_random_shot:
    Morgan "{i}Guess I'll just spray and pray and hope for the best.{/i}"
    "some montage of shots ricocheting but missed"
    Morgan "{i}As I thought, this challenge was impossible.{/i}"
    Morgan "{i}Guess I'll-URK!{/i}"

    Sarah "How disappointing."
    Sarah "I really hoped you'd be a worthy ally, but it turns out I was just wasting my time with you."
    Sarah "At least I'll get some satisfaction from taking your life with my own two hands."
    scene meeting with Fade(0.1, 0.0, 0.5, color="#fff")
    "..."
    Grandmaster "You can't expect anyone else to believe in you if you don't believe in yourself."
    Grandmaster "And when you're working with bona fide murderers, such a lack of confidence can be fatal."
    Grandmaster "Try again."
    "GAME OVER"

    jump sc_next_day
    return

label sc_timimg_shot:
    Morgan "{i}Wait, I know how to pull this off.{/i}"
    Morgan "{i}To be a true assassin, you need mastery over time itself.{/i}"
    Morgan "{i}How about I bend the very laws of causality in my favor?{/i}"
    Morgan "{i}First, I'll shoot the metal plate on the left.{/i}"
    Morgan "{i}Then the one on the right.{/i}"
    Morgan "{i}Then the one above me.{/i}"
    Morgan "{i}If I get the angles right, I'll have triangulated my way to a bullseye.{/i}"
    "Some montage of incredible timming or something that help the shots land correctly (I don't know, ask Mers lol)"
    Sarah "Wow, you actually did it."
    Sarah "This is amazing!"

    Morgan "Now am I good enough for you?"
    "Sarah blushes"
    Sarah "You are... if you want to be, that is."

    Morgan "{i}That's quite the invitation in her eyes.{/i}"
    Morgan "{i}But is this the kind of story I've been aspiring to?{/i}"

    menu:
        "Kiss her":
            jump sc_kiss_sarah
        "Keep it professional":
            jump sc_stay_professional
    return


label sc_stay_professional:
    Morgan "I'm afraid I'm not the kinda person to mix business with pleasure."
    Morgan "Sorry, Sarah."
    "Sarah looks disappointed for a bit before quickly composing herself."
    Sarah "So we're keeping this professional, then."
    Sarah "I can respect that."
    Sarah "Besides, we might be better off if we can fully focus on the next task at hand."

    Morgan "And what task would that be?"

    Sarah "Getting rid of one last pesky loose end."
    Sarah "My brother-in-law, Agent Graham, wants to bring me to justice for my so-called crimes."
    Sarah "I'm going to make sure he never gets the chance."
    Sarah "You in?"
    Morgan "Absolutely, lead the way"
    jump sc_track_graham


label sc_kiss_sarah:
    $ romance = True
    "Morgan and Sarah kiss with their arms wrapped around each other."
    "some montage of Morgan kissing Sarah {i}passionately{/i}"
    
    Morgan "{i}Yes, this is what I want.{/i}"
    Morgan "{i}I want her, all of her.{/i}"
    Morgan "{i}And now I can finally have her.{/i}"
    Morgan "{i}This is the best day of my life!{/i}"

    Morgan "{i}I see now why assassins seem to bend time so easily.{/i}"
    Morgan "{i}That rush of adrenaline made the kiss seem like a wonderful eternity, but it was just a few seconds long.{/i}"

    Sarah "Well, aren't you a good kisser? I'll at least give you that much."
    Sarah "And I'm glad to have you by my side as we finish things and tie up all loose ends."

    Morgan "And what loose ends are you referring to, exactly?"

    Sarah "Why my brother-in-law, of course."
    Sarah "Agent Graham is still out to get me, so we're going to get to him first."
    Sarah "You in?"

    Morgan "You're goddamn right I am"
    jump sc_track_graham
    return
