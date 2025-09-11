label sc_warehouse_trap:
    scene Warehouse
    show Morgan_default at left
    show Sarah at right
    Morgan "{i}I already get the feeling that things are going off-track.{/i}"
    Morgan "{i}Agent Graham should've already been here, but there's no sign of him.{/i}"
    Morgan "{i}Did we miss something?{/i}"

    if romance:
        Sarah "Hey babe, are you feeling okay?"
        Morgan "I don't know. I feel like we're walking into a trap here. We should've gotten the drop on Graham already."
        Sarah "(kisses Morgan) I know, my love. But no plan ever survives contact with the enemy."
        Sarah "Whatever happens next, we'll face it together. I love you."
        Morgan "Yeah, thanks for the pep talk, Sarah. I love you, too."
        "..."

    Sarah "So if Graham isn't here, then we—"
    # Flashbang
    Morgan "Shit, this really was a trap!"
    scene Warehouse with Fade(0.1, 1, 0.5, color="#fff")

    show Morgan_default:
        xalign 0.1
    show Sarah:
        xalign 0.2

    with Pause(0.2)
    
    Graham "Indeed it was."
    show Graham at right with moveinright
    "Graham looking smirkly while our protags feeling dissle. He take advantage of that and lock our protags up"
    Graham "Looks like you two tried to hunt me down in this warehouse after all, exactly as I planned."
    Graham "Now, as much as I'd like to bring you both to justice myself, I have bigger fish to fry, so I'll just have to leave that to the police arriving at the scene."

    Sarah "Really? Bigger fish than me, your own sister-in-law?!"

    Graham "Hate to break it to you, Sarah, but you're no longer worth my time, or your sister's for that matter."
    Graham "We both know you'll never change."
    Graham "It'll hurt to see you in the execution chamber, but it is what it is."
    "Graham left"
    hide Graham with dissolve
    "..."
    Morgan "Shit! Shit shit shit SHIT! How do we get out of these before the cops show up?!"

    if romance:
        Sarah "We'll figure it out together, darling. I won't let anything happen to you on my watch!"
    else:
        Sarah "How should I know?! You need to think fast, Morgan!"

    Morgan "{i}...What do I do, what do I do?!...{/i}"

    menu:
        "Wait for the cops to arrive and bluff my way out":
            jump sc_bluff_cops
        "If I can find a way to bend time again...":
            jump sc_bend_time
    return

label sc_bluff_cops:
    Morgan "We'll bluff our way out."

    Sarah "Huh? Are you serious?!"

    Morgan "There's not enough time for anything else, Sarah! Just trust me, alright?"
    "Some cops show up"
    show Cop at right with moveinright
    Cop "Right, this was the location the tip gave us. And look what we have here."
    Morgan "Officer, look, I can explain, just—"

    # Gunshot, fade to black
    scene Warehouse with Fade(0.1, 0.0, 0.2, color="#fff")
    Grandmaster "I'm sorry, Morgan, I had to order your termination."
    Grandmaster "There's no way you could've bluffed your way out of that situation, and I couldn't afford to let the cops take you in for interrogation."
    Grandmaster "You need to try this again, and choose a path that doesn't put me at risk."

    "..."
    jump sc_warehouse_trap

    return

label sc_bend_time:

    Morgan "{i}If only I could bend time to my will, I could get me and Sarah out of this!{/i}"
    Morgan "{i}Just how did I do it the last time?!{/i}"
    Morgan "{i}Wait... maybe if I just...{/i}"
    "Morgan do some magic, time bending stuffs and get out of the chains. (ask Mers pls)"
    Morgan "Come on, we need to move!"

    Sarah "How did you do that? You slipped free like it was nothing!"

    Morgan "An assassin needs to bend time, right?"
    Morgan "The trouble with zip-ties isn't that they're impossible to break, it's just the time and effort needed for that is too much."
    Morgan "But if I can change that, bend time to my will..."

    Sarah "You're special, Morgan. This isn't a power most people have."

    Morgan "I see... I've always wondered why the Grandmaster saw so much potential in me."
    Morgan "Maybe this is what she meant..."

    if romance:
        # Sarah kisses Morgan
        Morgan "Whoa, Sarah!"
        "Sarah suddenly go in for a kiss????"
        " (not sure. I add that so that the next dialogs at least make some sense)"
        Sarah "I love you! I love you, I love you, I love you! I'm so glad you're safe!"
        Morgan "I'm glad you're safe too, Sarah. We really are unstoppable, aren't we?"
        Sarah "(tearfully) Yeah, we really are. We're going to conquer this world, my love. Just the two of us."
        Morgan "You're goddamn right, darling. You're goddamn right."
    else:
        Sarah "The Grandmaster is truly remarkable, isn't she? I'm in awe."
        Morgan "Yeah. I've spent my whole life devoted to her, and I still fail to grasp the depths of her brilliance."

    Sarah "So, now that we're clear, we need to find Graham. Any idea where he could be?"

    Morgan "He mentioned having bigger fish to fry, didn't he? That could only mean one thing."

    Morgan "He's going after June Davidson herself!"

    jump sc_june_headquarters
    return

label sc_june_headquarters:

    Morgan "He's going to ambush your boss, Sarah. He's going to take out June Davidson."

    Sarah "If he managed to get the drop on us, he could get the drop on June too. I need to call her."

    Morgan "Looks like my hunch was right."

    Sarah "We need to get to the Davidson Solutions headquarters, ASAP!"
    "Montage of them running..."
    scene HQ 
    "Scene change to June\'s HQ"
    "They finally catch up to Graham"
    show Graham at center
    with Pause(0.3)
    show Morgan_default:
        xalign 0.1
    show Sarah:
        xalign 0.2

    with Pause(0.2)
    show Graham at right with moveinleft
    
    Graham "Tch. Looks like I underestimated you two. But it doesn't matter. I'll bring everyone to justice all at once!"

    Morgan "{i}This is it, the moment where I finally take Agent Graham down.{/i}"
    Morgan "{i}And knowing who I am now, this is what I'll do.{/i}"

    if romance:
            Morgan "{i} I'll strike first and strike hard. No mercy! {/i}"
            jump sc_romance_climax
    else:
        Morgan "{i} I need to take him alive for the Grandmaster {/i}"
        jump sc_assassin_climax
    

    return


