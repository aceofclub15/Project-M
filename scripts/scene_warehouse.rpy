label sc_warehouse_trap:
    $ persistent.story_tree["assassin5"]["unlocked"] = True
    scene black
    show bg warehouse_interior
    "Morgan wakes up the next day, dressed in black coveralls as she and Sarah infiltrate the Hallex warehouse."
    show Morgan_default at left
    show Sarah at right
    $ voice_line("m","hmm","sad")
    Morgan "{i}I already get the feeling that things are going off-track.{/i}"
    Morgan "{i}Agent Graham should've already been here, but there's no sign of him. Did we miss something?{/i}"


    if romance:
        $ voice_line("s", "so", "bad")
        Sarah "Hey babe, are you feeling okay?"
        $ voice_line("m","uh","bad")
        Morgan "I don't know. I feel like we're walking into a trap here. We should've gotten the drop on Graham already."
        $ voice_line("s","yeah","hap")
        Sarah "I know, my love. But no plan ever survives contact with the enemy. Whatever happens next, we'll face it together. I love you."
        $ voice_line("m","yeah","sad")
        Morgan "Yeah, thanks for the pep talk, Sarah. I love you, too."
        "..."

    $ voice_line("s","so","bad")
    Sarah "So if Graham isn't here, then we..."
    # Flashbang
    $ voice_line("m","shit","sur")
    Morgan "Then it must be a trap!"

    scene bg warehouse_interior with Fade(0.1, 1, 0.5, color="#fff")
    "A flashbang grenade is dropped, and the screen goes white. When the white noise clears, Morgan and Sarah are restrained with zip-ties."
    show Morgan_default at left
    show Sarah:
        xalign 0.3

    with Pause(0.2)
    
    # Graham appears
    show Graham at right with moveinright
    $ voice_line("g","hah","hap")
    Graham "Looks like you two tried to hunt me down in this warehouse after all, exactly as I planned."
    $ voice_line("m","shit","dis")
    Morgan "Shit, this really was a trap!"
    $ voice_line("g", "well", "hap")
    Graham "Indeed it was. Now, as much as I'd like to bring you both to justice myself, I have bigger fish to fry, so I'll just have to leave that to the police arriving at the scene."
    $ voice_line("s", "so", "ang")
    Sarah "Really? Bigger fish than me, your own sister-in-law?!"
    $ voice_line("g", "ugh", "dis")
    Graham "Hate to break it to you, Sarah, but you're no longer worth my time, or your sister's for that matter. We both know you'll never change. It'll hurt to see you in the execution chamber, but it is what it is."
    "Graham gets up and walks away, leaving Morgan and Sarah behind."
    hide Graham with dissolve
    "..."
    $ voice_line("m","shit","sur")
    Morgan "Shit! Shit shit shit SHIT! How do we get out of these before the cops show up?!"
    if romance:
        $ voice_line("s","well","hap")
        Sarah "We'll figure it out together, darling. I won't let anything happen to you on my watch!"
    else:
        $ voice_line("s", "yeah", "ang")
        Sarah "How should I know?! You need to think fast, Morgan!"
    $ voice_line("m","hmm","sad")
    Morgan "{i}...What do I do, what do I do?!{/i}"

    menu:
        "Wait for the cops to arrive and bluff my way out":
            $ persistent.story_tree["bluff"]["unlocked"] = True
            jump sc_bluff_cops
        "If I can find a way to bend time again...":
            $ persistent.story_tree["bend_time"]["unlocked"] = True
            jump sc_bend_time
    return

label sc_bluff_cops:
    $ voice_line("m","yeah","sad")
    Morgan "We'll bluff our way out."
    $ voice_line("s", "yeah", "ang")
    Sarah "Huh? Are you serious?!"
    $ voice_line("m","tch","ang")
    Morgan "There's not enough time for anything else, Sarah! Just trust me, alright?"
    show Cops at right with moveinright

    Cop "Right, this was the location the tip gave us. And look what we have here."
    $ voice_line("m","well","bad")
    Morgan "Officer, look, I can explain, just—"
    "Before Morgan can finish her sentence..."
    # Gunshot, fade to black
    $ voice_line("m","ah","ang")
    scene bg warehouse_interior with Fade(0.1, 0.0, 0.2, color="#fff")
    "A bullet fly from afar through the windows glass and hit Morgan\'s head"
    scene black
    $ voice_line("gm","well","sad")
    Grandmaster "I'm sorry, Morgan, I had to order your termination."
    Grandmaster "There's no way you could've bluffed your way out of that situation, and I couldn't afford to let the cops take you in for interrogation."
    $ voice_line("gm","so","bad")
    Grandmaster "You need to try this again, and choose a path that doesn't put me at risk."
    "GAME OVER"
    jump sc_warehouse_trap
    return

label sc_bend_time:
    $ persistent.story_tree["assassin6"]["unlocked"] = True

    $ voice_line("m","hmm","bad")
    Morgan "{i}If only I could bend time to my will, I could get me and Sarah out of this. Just how did I do it the last time?!{/i}"
    $ voice_line("m","oh","sur")
    Morgan "{i}Oh wait... maybe if I just...{/i}"
    "Morgan shifts to a trance state as they miraculously loosen the zip-tie in seconds. Morgan then does the same with Sarah."
    Morgan "Come on, we need to move!"
    "Morgan escapes the warehouse with Sarah, as the cops arrive to find an empty warehouse."
    "The scene shifts to Morgan and Sarah facing each other."
    $ voice_line("s", "ah", "hap")
    Sarah "How did you do that? You slipped free like it was nothing!"
    $ voice_line("m","well","hap")
    Morgan "An assassin needs to bend time, right? The trouble with zip-ties isn't that they're impossible to break, it's just the time and effort needed for that is too much. But if I can change that, bend time to my will..."

    $ voice_line("s", "yeah", "hap")
    Sarah "You're special, Morgan. This isn't a power most people have."
    $ voice_line("m","oh","ang")
    Morgan "I see... I've always wondered why the Grandmaster saw so much potential in me. Maybe this is what she meant..."

    if romance:
        # Sarah kisses Morgan
        "Sarah rushes and kisses Morgan"
        
        $ voice_line("m","whoa","hap")
        Morgan "Whoa, Sarah!"
        $ voice_line("s","yeah","hap")
        Sarah "I love you! I love you, I love you, I love you! I'm so glad you're safe!"
        $ voice_line("m","yeah","sad")
        Morgan "I'm glad you're safe too, Sarah. We really are unstoppable, aren't we?"
        $ voice_line("s","yeah","hap")
        Sarah "Yeah, we really are. We're going to conquer this world, my love. Just the two of us."
        $ voice_line("m","right","hap")
        Morgan "You're goddamn right, darling. You're goddamn right."
    else:
        $ voice_line("s", "so", "hap")
        Sarah "The Grandmaster is truly remarkable, isn't she? I'm in awe."
        $ voice_line("m","yeah","sad")
        Morgan "Yeah. I've spent my whole life devoted to her, and I still fail to grasp the depths of her brilliance."
        
    $ voice_line("s","so","bad")
    Sarah "So, now that we're clear, we need to find Graham. Any idea where he could be?"
    $ voice_line("m","hmm","sad")
    Morgan "He's going to ambush your boss, Sarah. He's going to take out June Davidson."
    
    jump sc_june_headquarters
    
    return

label sc_june_headquarters:
    $ voice_line("s", "no", "ang")
    Sarah "If he managed to get the drop on us, he could get the drop on June too. I need to call her."
    "Sarah calls June, but there's no response."
    $ voice_line("m","tch","ang")
    Morgan "Looks like my hunch was right."
    $ voice_line("s", "no", "ang")
    Sarah "We need to get to the Davidson Solutions headquarters, ASAP!"
    "Morgan and Sarah get in Sarah's car and drive to Davidson Solutions HQ. Luckily, they manage to catch up to him."
    scene black
    show bg headquarters
    "Scene change to Davidson Solutions Headquarters" #June's HQ
    show Graham at center
    with Pause(0.3)
    show Morgan_default at left
    show Sarah:
        xalign 0.2

    with Pause(0.2)
    show Graham at right with moveinleft
    
    $ voice_line("g","tch","bad")
    Graham "Tch. Looks like I underestimated you two. But it doesn't matter. I'll bring everyone to justice all at once!"
    $ voice_line("m","hmm","dis")
    Morgan "{i}This is it, the moment where I finally take Agent Graham down.{/i}"
    Morgan "{i}And knowing who I am now, this is what I'll do.{/i}"

    if romance:
            Morgan "{i} I'll strike first and strike hard. No mercy! {/i}"
            jump sc_romance_climax
    else:
        Morgan "{i} I need to take him alive for the Grandmaster {/i}"
     
    jump sc_assassin_climax
    

    return