label sc_graham_paid:
    Morgan "Oh, but I think you were paid, Graham."
    Graham "{i}What's that supposed to mean? Are you calling me a liar?!{/i}"
    Morgan "No, not you. A covert job means a covert payment. You should've received a set of coordinates to a dead drop. 
    But you didn't, because your partner Adam took it all for himself."
    Graham "{i}But why? Why would he do that?{/i}"
    Morgan "Well, for one thing, Adam's the CEO of a billion-dollar company, and you're not.
    I wonder what Hallex works on. I wonder how Adam got rich."
    Graham "{i}Oh my God, that son of a bitch! He told me the intel we got on Warlord Hakim's bioweapon was bogus. But if he lied to me...{/i}"
    Morgan "Then he cut you out, and used the knowledge from the mission to enrich himself at your expense. 
    And it seems like you're not the only person he screwed over."
    Graham "{i}So that's why Davidson Solutions put a kill order on him. We need to investigate the Hallex corporation, pronto.{/i}"
    Morgan "Any idea where to start?"
    Graham "{i}Yeah. Adam has a warehouse in Queens. If we're going to find out what he's hiding, we have to go there.{/i}"
    jump sc_hallex_warehouse_ambush
    return


label sc_hallex_warehouse_ambush:
    "Morgan and Graham arrive at the Hallex warehouse, where they catch Adam in the act of trying to smuggle away a cargo box."
    scene warehouse_interior
    show Adam at right
    show Graham at topleft with moveinleft
    show Morgan_default at left with moveinleft

    Graham "Adam! Stop right where you are!"
    "Adam notices Graham and Morgan approaching him, and his expression turns hostile as he faces off against them alongside his bodyguard."
    Adam "Tch. And to think I was just a few seconds away from cleaning this mess up."
    Morgan "What do you mean by that, Adam? Covering up your crimes? Running away from the people you screwed over, present company included!"
    "Morgan points to Graham."
    Graham "I'm going to make sure you pay for what you did back in Afghanistan, Adam, and I suggest you come quietly for your own sake."
    Adam "Go to hell."
    Morgan "You really don't want to push your luck here. If me and Graham found out about this place, it's only a matter of time before-"
    "A series of gunshots ring out as Sarah arrives on the scene and kills Adam's bodyguard. Adam quickly runs away and hides."
    show Sarah at topright with moveinbottom
    Sarah "Sorry to crash the party, everyone, but I'm afraid I have a contract to fulfill. Besides, my master would like a word with you."
    "Sarah's boss, June Davidson, appears alongside her, looking smug and self-assured."
    show June at center with moveinbottom
    June "Hello, Morgan and Graham. It's a pleasure to finally meet you both in person."
    Graham "Can the pleasantries, June. Why the hell are you here?"
    June "To propose a truce. You and I both have a common enemy, now that you've seen firsthand what a repugnant weasel Adam Roarke is. Let's work together, in the interests of justice."
    Graham "You? A fighter for justice?! Give me a break. Adam may be a corrupt backstabbing weasel, but you've killed hundreds of people just to line your bank account."
    Graham "Besides, the only reason you hired Sarah was to lure me out of hiding so you could kill me too, right? Was that for the sake of justice too?!"
    "Morgan discreetly sneaks away to find a hidden vantage point in a corner."
    hide Morgan_default with dissolve
    "June turns to face Adam"
    June "(Sigh...)You disappoint me, Adam. If you'd just gone along with my idea, I would've ensured that Sarah backstabbed you quickly and painlessly. Now I'm going to have to make it HURT!"

    jump sc_ambush
    return


label sc_ambush:
    "..."
    "Morgan swiftly attacks Sarah from behind with a sneaky kick, incapacitating her. Adam takes the opportunity to fire a precision shot, which kills Sarah instantly."
    show Morgan_default at topright with moveintop
    hide Sarah
    show Adam at right
    "The two then gang up on June and hold her at gunpoint."
    June "No, no NO! This can't be happening, you can't beat me so easily, I-"
    "A gunshot rings out from Adam's gun and June collapses."   
    show June:
        rotate 90
    Adam "Looks like the hunter became the hunted. So long, you bitch! Hahahaha!"
    hide June
    show Adam at center with moveinright
    "Graham aims his gun at Adam, leading to a standoff."
    Graham "Yeah, we got rid of the assassins, but you won't escape justice! Morgan, if you will."
    "Morgan takes out a video camera, which was secretly filming everything since her and Graham's arrival at the warehouse."
    Morgan "Graham and I made this contingency plan in case we died out here. Your crimes have already been broadcast to the entire public, Adam, and exposing June and Sarah was a nice bonus too. Graham and I are going to be hailed as citizen journalism heroes, while you're going to spend the rest of your life paying for everything you've done."
    Adam "No! NO! I'm not going to prison! I'D RATHER DIE!"
    "Adam suddenly turns his gun on himself and pulls the trigger before Morgan or Graham have time to react."
    show Adam:
        rotate 90
    Graham "Shit! The bastard killed himself!"
    Morgan "In any case, the bad guys are dead. I'd say justice is served, even if it's not in the way we'd have liked."
    Graham "Maybe you're right. Still, I wish we'd learned more about who else Adam ripped off. I hate knowing that those bastards are still at large."
    Morgan "Even if they are, they're going to be very unhappy about Adam's crimes being made public. It's only a matter of time before the authorities snuff out all the collaborators."
    Graham "Yeah, there's no way anyone gets away with their crimes now, but our part in this scandal's over. So, what do we do next?"
    
    Morgan "We make a good team. Why break it up?"
    jump sc_ace_epilogue
    return

label sc_ace_epilogue:
    scene japanese_restaurant
    "Time skips ahead by three months, with Morgan and Graham eating ramen at a Japanese restaurant while the news plays on TV."
    "News broadcast: In shocking news, billionaire venture capitalist Marcus Simms was found dead in his home today when the FBI conducted a raid on his mansion in connection with the Hallex scandal. Authorities conclude it was a suicide by hanging."
    Graham "Marcus Simms. So that's who Adam sold America's secrets to."
    Morgan "Seems that way. The two must've had a falling out, which is why Marcus put out a kill order and dragged us both into this mess."
    Graham "At least the authorities proved equal to the challenge and finished what the two of us started. A surprise to be sure, but a welcome one."
    Morgan "Still, I don't think Marcus acted alone. I wish we could've uncovered everyone he was working with."
    Graham "That's life for you. There's almost never any clean and easy solutions. Still, now that everything's squared up, we can fully focus on the task at hand."
    Morgan "You mean the case of the missing parrot? I knew the Morgan & Graham detective agency wouldn't take any fancy cases right off the bat, but this is bottom of the barrel stuff."
    Graham "I think the Grandmaster really spoiled you, you know. You're way too used to excitement. But you'll learn the value of hard work and patience eventually, I'll make sure of that."
    "Morgan smiles playfully and kisses Graham on the cheek."
    Morgan "I'm sure you will. Oh, and I'm paying the bill this time."
    "Camera pans out and fades to black."
    "Detective route ace epilogue unlocked."
    $ persistent.ace_ending = True
    return