label sc_target_poisoned:
    # Existing voice line for an internal thought, keeping it as is or removing based on typical workflow, but let's assume internal dialogue doesn't need external voice_line updates unless specified.
    $ voice_line("m","so","ang")
    Morgan "{i}Looks like I'm siding with the psychopathic murderer.{/i}"
    $ voice_line("m","yeah","sad")
    Morgan "{i}And I can't deny there's a certain thrill to being a villain here.{/i}"
    Morgan "{i}Sarah, show me what you've got.{/i}"
    scene black
    show bg hotel_restaurant
    show Adam at right
    with Pause(0.2)
    show Sarah_disguise at left with moveinleft
    $ voice_line("s", "well", "hap")
    Sarah "Your order, sir."
    $ voice_line("a", "hmm", "sur")
    Adam "Yes, thanks."

    "Adam is gulping down the drink, when Sarah gracefully leaves the dining area." 
    scene black
    show bg hoteln with dissolve
    show Sarah_disguise at right
    show Morgan_default at left
    $ voice_line("m","well","bad")
    Morgan "Evening ma'am, mind if I have a word?"
    $ voice_line("s", "yeah", "ang")
    Sarah "I'm sorry, can I help you with something?"
    "Morgan leans into Sarah's ear."
    show Morgan_default at center with moveinleft
    $ voice_line("m","so","bad")
    Morgan "Listen carefully and keep cool. You're being followed and someone's come here to apprehend you."

    $ voice_line("s", "so", "ang")
    Sarah "What? How do you know this?!"
    $ voice_line("m","right","bad")
    Morgan "Does the name Graham ring a bell?  I have a recording of him knocking out your handler at the lounge."
    $ voice_line("s", "hmmph", "ang")
    Sarah "Shit! If he's the one who found me, I'm in serious trouble."
    $ voice_line("s", "sigh", "sad")
    Sarah "I don't exactly trust you right now, but I can't risk ignoring this."
    Sarah "Do you have anything else for me?"

    $ voice_line("m","yes","ang")
    Morgan "Yes. I have an alternate extraction route prepped and ready at the behest of my master."
    Morgan "That should throw Graham off your trail, and we can rendezvous sometime later."
    "Rourke convulses under the effect of the poison as he's hastily ushered out."
    $ voice_line("m","oh","sur")
    Morgan "Looks like things are escalating. What's your decision, Sarah?"
    $ voice_line("s", "yeah", "ang")
    Sarah "Fine. Give me the coordinates, quickly."

    "Morgan sends the new extraction coordinates to Sarah."
    $ voice_line("s", "so", "sad")
    Sarah "I got them. I hope I can trust you."
    Morgan "Now go, quickly!"
    with Pause(0.5)
    scene black 
    "Sarah and Morgan part ways. Then the Grandmaser calls Morgan."
    show hologram_GM:
        xalign 0.5
        yalign 0.5
    $ voice_line("gm","so","hap")
    Grandmaster "So you've chosen to aid and abet a assassin, have you?"
    $ voice_line("gm","well","sad")
    Grandmaster "Well, I just wanted to let you know that Adam's death has been confirmed and Sarah has arrived at the exit point, safe and sound."
    Grandmaster "I have also given her your contact information and told her to contact you tomorrow. It's time for you to see this through to the end."
    $ voice_line("m","yeah","sad")
    Morgan "Thank you, Grandmaster. I promise I won't disappoint."
    $ voice_line("gm","good","hap")
    Grandmaster "I know you won't, Morgan. Until next time."
    $ voice_line("m","yeah","sad")
    Morgan "{i}I've made my decision, now it's time to see where it takes me.{/i}"
    Morgan "{i}I'm looking forward to hearing from Sarah again.{/i}"

    jump sc_next_day
    return



label sc_next_day:
    show bg shooting_range
    "The next day, Morgan is in her office and recieves an message from Sarah."
    $ voice_line("m","so","bad")
    Morgan "{i}Sarah told me to meet her, alone, at a deserted shooting range.{/i}"
    $ voice_line("m","hmm","sad")
    Morgan "{i}Being asked to come alone is already a red flag, but I did willingly choose the path of danger after all.{/i}"
    $ voice_line("m","oh","sur")
    Morgan "Hello Sarah. Looks like you made it out of the last job safely."
    show Sarah at right with moveinright
    $ voice_line("s", "so", "hap")
    Sarah "I did. You were true to your word."
    Sarah "I still don't know why you helped me though."
    $ voice_line("m","yes","hap")
    Morgan "The answer to that is simple - because I wanted to."
    $ voice_line("s", "yeah", "ang")
    Sarah "And your master just lets you go around doing whatever you want?"
    $ voice_line("m","well","hap")
    Morgan "In a manner of speaking."
    $ voice_line("s", "so", "ang")
    Sarah "You've just made yourself an accomplice to a high-profile assassination."
    Sarah "You do seem to have the stomach for my line of work, but whether you have the skill is another question entirely."
    $ voice_line("s", "so", "hap")
    Sarah "Show me you have what it takes Morgan, and we can do great things together."
    $ voice_line("m","what","sur")
    Morgan "I already helped you get away with murder, isn't that good enough for you?"
    $ voice_line("s", "so", "ang")
    Sarah "I decide what's good enough for me."
    $ voice_line("s", "hmmph", "ang")
    Sarah "Now, are you going to hit the target or not?"
    Morgan "{i}The challenge she's set up is ridiculous. She wants me to curve the bullet around obstables.{/i}"
    $ voice_line("m","tch","ang")
    Morgan "{i}How the hell am I supposed to pull this off?{/i}"

    menu:
        "Maybe the key is to control time itself":
            $ persistent.story_tree["master_time"]["unlocked"] = True
            jump sc_timimg_shot
        "There's no way I can do this":
            $ persistent.story_tree["hope_shot"]["unlocked"] = True
            jump sc_random_shot
    return


label sc_random_shot:
    Morgan "{i}This truly is impossible. I'll just spray and pray and hope for the best.{/i}"
    "Sounds of gunshots ring out, but none hit the target."
    $ voice_line("m","tch","ang")
    Morgan "{i}As I thought, this challenge was impossible.{/i}"
    Morgan "{i}Guess I'll-{/i}"
    $ voice_line("m","ah","dis")
    "Morgan is shot from behind."
    scene black with Fade(0.1, 0.0, 0.5, color="#fff")
    $ voice_line("s","sigh","sad")
    Sarah "How disappointing."
    Sarah "I really hoped you'd be a worthy ally, but it turns out I was just wasting my time with you."
    Sarah "At least I'll get some satisfaction from taking your life with my own two hands."
    scene black
    $ voice_line("gm","well","ang")
    Grandmaster "You can't expect anyone else to believe in you if you don't believe in yourself."
    Grandmaster "And when you're working with bona fide assassin, such a lack of confidence can be fatal."
    Grandmaster "Try again."
    "GAME OVER"

    jump sc_next_day
    return



label sc_stay_professional:
    $ voice_line("m","no","ang")
    Morgan "I'm afraid I'm not the kinda person to mix business with pleasure."
    Morgan "Sorry, Sarah."
    "Sarah looks disappointed then quickly composes herself."
    $ voice_line("s", "oh", "hap")
    Sarah "So we're keeping this professional, then."
    Sarah "I can respect that."
    Sarah "Besides, we might be better off if we can fully focus on the next task at hand."
    $ voice_line("m","what","sur")
    Morgan "And what task would that be?"
    $ voice_line("s", "so", "ang")
    Sarah "Getting rid of one last pesky loose end."
    Sarah "My brother-in-law, Graham wants to bring me to justice for my so-called crimes. I'm going to make sure he never gets the chance."
    Sarah "You in?"
    $ voice_line("m","yes","ang")
    Morgan "Absolutely, lead the way."
    jump sc_track_graham


label sc_kiss_sarah:
    $ romance = True
    "Morgan and Sarah kiss with their arms wrapped around each other."
    $ voice_line("m","yes","hap")
    Morgan "{i}Yes, this is what I want. I want her, all of her.{/i}"
    Morgan "{i}And now I can finally have her. This is the best day of my life!{/i}"

    
    # Internal dialogue, no external voice line update needed
    $ voice_line("m","oh","ang")
    Morgan "{i}I see now why assassins seem to bend time so easily.{/i}"
    Morgan "{i}That rush of adrenaline made the kiss seem like a wonderful eternity, but it was just a few seconds long.{/i}"

    $ voice_line("s","well","hap")
    Sarah "Well, aren't you a good kisser? I'll at least give you that much."
    Sarah "And I'm glad to have you by my side as we tie up all loose ends."
    $ voice_line("m","huh","sur")
    Morgan "And what loose ends are you referring to, exactly?"
    $ voice_line("s","hmmph","ang")
    Sarah "Why my brother-in-law, of course. Graham is still out to get me, so we're going to get to him first."
    $ voice_line("m","so","sad")
    Sarah "You in?"
    
    $ voice_line("m","yes","hap")
    Morgan "You're damn right I am!"
    jump sc_track_graham
    return