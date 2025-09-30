label sc_grandmaster_route_start:
    scene black
    show bg japanese_restaurant
    $ renpy.music.set_volume(0.3, channel='channel_background')
    "The Grandmaster waits at a high-class restaurant. A woman arrives and sits at her table. It's June Davidson."
    Grandmaster "{i}Thanks to agent Morgan's efforts, I was finally able to put all the pieces of this messy story together. And now, with the information I have...{/i}"

    menu:
        "I can finally save the woman I love":
            jump sc_grandmaster_romance_ending
        "I can finally save the best friend I've ever known":
            jump sc_grandmaster_friendship_ending
    return

label sc_grandmaster_romance_ending:
    $ relationship_type = "romance"
    jump sc_grandmaster_ending
    return

label sc_grandmaster_friendship_ending:
    $ relationship_type = "friendship"
    jump sc_grandmaster_ending
    return

label sc_grandmaster_ending:
    show June at right with moveinleft
    if relationship_type == "romance":
        "The Grandmaster smiles as she sees June, and the two kiss."
        $ voice_line("gm","ah","hap")
        Grandmaster "I'm glad you made it, honey."
    elif relationship_type == "friendship":
        "The Grandmaster smiles as she sees June, and the two shake hands."
        Grandmaster "I'm glad you made it, June."
    
    $ voice_line("j", "well", "hap")
    June "You know I could never say no to you, January."
    "The two settle down as the waiter serves a steak tartare to each of them."
    show January at left with dissolve
    $ voice_line("j", "hmmph", "dis")
    June "So, what did you learn? How do I prevent my death?"
    $ voice_line("gm","so","fea")
    January "Adam is trying to double-cross Marcus Simms and the Executive Board of LambdaCorp over the deal with Warlord Hakim's bioweapon. 
    They're the ones who've ordered his death."
    $ voice_line("j", "oh", "hap")
    June "Oh, so that's who Emissary Wallace represents. But I really don't want to turn down their paycheck. 
    How exactly do things go wrong, January?"
    $ voice_line("gm","so","dis")
    January "Well, I'd advise against going after Graham. He's the architect of your downfall in both the timelines I explore."
    $ voice_line("gm","okay","dis")
    January "Either Graham works with Morgan in the detective timeline to take you down, or he manages to find a way to your headquarters before the assassin timeline's Morgan finally defeats him."
    $ voice_line("gm","so","dis")
    January "Which still won't matter because-"
    $ voice_line("j", "oh", "fea")
    June "Marcus and LambdaCorp will execute me for my incompetence."
    "June smiles in relief."
    if relationship_type == "romance":
        $ voice_line("j", "thanks", "sad")
        June "Thanks for everything you've done, my love. I'm so lucky to have you."
        "June and January kiss."
    elif relationship_type == "friendship":
        $ voice_line("j", "thanks", "hap")
        June "Thanks for everything you've done, January. I don't know where I'd be without you."
        "January smiles warmly."
    $ voice_line("gm","heh","hap")
    January "Anytime, June. After all, it's only thanks to training under you that I built Ouroboros into the vast agency that it is today. "
    $ voice_line("gm","so","dis")
    January "But when I learned that I could traverse alternate timelines and you couldn't, it didn't feel right that I started surpassing you, you know?"
    
    if relationship_type == "friendship":
        $ voice_line("j", "hah", "bad")
        June "Don't get too full of yourself now, it's not like I'm jealous. After all, it's only thanks to you that I've lasted as long as I have. Both of us need each other."
    elif relationship_type == "romance":
    $ voice_line("j", "well", "hap")
        June "Oh, Jan, I'm not jealous of you. After all, it's only thanks to you that I've lasted as long as I have. Both of us need each other."
    
    $ voice_line("gm","yes","ang")
    January "Yeah. We're both ruling the world together but we'd both fall apart on our own."
    if relationship_type == "romance":
        $ voice_line("gm","heh","hap")
        January "But even aside from that, I love you, June. I'd be happy in any timeline where we live long lives together."
        $ voice_line("j", "well", "sad")
        June "So would I."
        "June and January go to January's home, following which they spend the night together."
        January "{i}Growing up, I'd felt so alone. So isolated. I thought nobody would ever understand me, or see the world the same way I did. But June does. And more than that, she appreciates me. A quiet life with her means more than any victory I've ever tasted in the other timelines.{/i}"
        "A panel shows January and June together, with January wrapping one arm around June as they're covered with a bedsheet."
    elif relationship_type == "friendship":
        $ voice_line("gm","heh","hap")
        January "And that's why I'll always find a way to save you, June."
        $ voice_line("j", "thanks", "hap")
        June "And for that, I am forever grateful."
        "June and January go to January's home, following which they have a sleepover party."
        January "{i}Growing up, I'd felt so alone. So isolated. I thought nobody would ever understand me, or see the world the same way I did. But June does. My friendship with her means more than any victory I've tasted in the other timelines.{/i}"
        "A panel shows January and June together in casual pajamas. January's lazing back on her bed while June is relaxing on the couch."
    
    $ voice_line("j", "hmmph", "dis")
    June "Are you sure we should leave Graham alone, though? I still can't shake the feeling that he'll remain a loose end."
    $ voice_line("gm","well","ang")
    January "You leave that matter to me. I'll use my Enforcer 0, Campanella, to take care of him."
    $ voice_line("j", "well", "bad")
    June "But if you're using Campanella, then..."
    $ voice_line("gm","so","dis")
    January "Yup, he's loyal, so he won't go off and do his own thing. I know it goes against the spirit of what Ouroboros is supposed to be, but if it means saving your life, then..."
    
    if relationship_type == "romance":
        "June cuts off January with a kiss."
        $ voice_line("j", "thanks", "sad")
        June "Thank you, January. I...I wish I could find a way to make it up to you."
    elif relationship_type == "friendship":
        $ voice_line("j", "thanks", "hap")
        June "You're really going above and beyond for me, January. I wish I could find a way to make it up to you."
    "January gives a playful smile."
    $ voice_line("gm","ah","hap")
    January "Hmm, maybe you can."
    "June smiles nervously."
    $ voice_line("j", "oh", "fea")
    June "I'm not sure I like where this is going..."
    $ voice_line("gm","well","hap")
    January "But well, my backlog is piled up so high, June. I just keep jumping from one project to another and never finish anything."
    $ voice_line("gm","so","hap")
    January "If you really want to make it up to me, maybe you can take a break from your own work and become my manager for a change. I've seen Sarah's capabilities, she'll do an excellent job managing Davidson Solutions in your absence."
    $ voice_line("j", "well", "sad")
    June "But I like my job as CEO. It's so comfortable with you covering for me."
    $ voice_line("gm","heh","hap")
    January "I know, and I don't regret spoiling you one bit. But come on, June, this idea must excite you a little. Stepping into my domain, seeing how I live my life day to day, isn't this something you've been waiting for?"
    
    if relationship_type == "romance":
        "June smiles and kisses January."
        $ voice_line("j", "well", "hap")
        June "It is. You've got yourself a deal, honey. But don't think I'll go easy on you."
    elif relationship_type == "friendship":
        "June smiles warmly."
        $ voice_line("j", "hah", "bad")
        June "It is. You've got yourself a deal, friendo. But don't think I'll go easy on you."
    
    $ voice_line("gm","heh","hap")
    January "Believe me, with the backlog my ADHD has racked up, I don't want you to."
    "June and January laugh warmly alongside each other as the scene fades to black. The time skips to next week, where they're both in the Grandmaster's chambers that have an ethereal background, as she begins her next mission."
    $ voice_line("gm","wait","ang")
    January "The Zephyr artifact retrieval? Really? But that's such a simple and boring mission."
    $ voice_line("j", "ugh", "sad")
    June "And one that'll blow up in your face if you don't finish it on time. No excuses, January."
    January "{i}I guess I shouldn't be surprised at how well June's adjusted to her new role, given the way she's led Davidson Solutions all these years. {/i}"
    January "{i}And despite my grumbling, she and I both know I wouldn't want things any other way.{/i}"
    $ voice_line("gm","well","hap")
    January "Fiiine, I'll initiate the timeline dive."
    January "{i}I see June looking at me with a childlike excitement as I power up the timeline generator interface. {/i}"
    January "{i}When the Zephyr artifact mission map loads up, my human vulnerability fades away, and I remember that I'm the Grandmaster of Ouroboros, and of destiny itself.{/i}"
    $ voice_line("gm","hmmph","bad")
    Grandmaster "Now, which Enforcer should I use this time?"
    
    return