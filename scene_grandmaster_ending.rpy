label sc_grandmaster_route_start:
    scene restaurant
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
    if relationship_type == "romance":
        "The Grandmaster smiles as she sees June, and the two kiss."
        Grandmaster "I'm glad you made it, honey."
    elif relationship_type == "friendship":
        "The Grandmaster smiles as she sees June, and the two shake hands."
        Grandmaster "I'm glad you made it, June."
    
    June "You know I could never say no to you."
    "The two settle down as the waiter serves a steak tartare to each of them."
    June "So, what did you learn? How do I prevent my death?"
    January "Adam is trying to double-cross Marcus Simms and the Executive Board of LambdaCorp over the deal with Warlord Hakim's bioweapon. They're the ones who've ordered his death."
    June "Oh, so that's who Emissary Wallace represents. But I really don't want to turn down their paycheck. How exactly do things go wrong, January?"
    January "Well, I'd advise against going after Graham. He's the architect of your downfall in both the timelines I explore."
    January "Either Graham works with Morgan in the detective timeline to take you down, or he manages to find a way to your headquarters before the assassin timeline's Morgan finally defeats him."
    January "Which still won't matter because-"
    June "Marcus and LambdaCorp will execute me for my incompetence."
    "June smiles in relief."
    if relationship_type == "romance":
        June "Thanks for everything you've done, my love. I'm so lucky to have you."
        "June and January kiss."
    elif relationship_type == "friendship":
        June "Thanks for everything you've done, January. I don't know where I'd be without you."
        "January smiles warmly."
    January "Anytime, June. After all, it's only thanks to training under you that I built Ouroboros into the vast agency that it is today. But when I learned that I could traverse alternate timelines and you couldn't, it didn't feel right that I started surpassing you, you know?"
    June "Oh, darling, I'm not jealous of you. After all, it's only thanks to you that I've lasted as long as I have. Both of us need each other."
    January "Yeah. We're both ruling the world together but we'd both fall apart on our own."
    if relationship_type == "romance":
        January "But even aside from that, I love you, June. I'd be happy in any timeline where we live long lives together."
        June "So would I."
        "June and January go to January's home, following which they spend the night together."
        January "{i}Growing up, I'd felt so alone. So isolated. I thought nobody would ever understand me, or see the world the same way I did. But June does. And more than that, she appreciates me. A quiet life with her means more than any victory I've ever tasted in the other timelines.{/i}"
        "A panel shows January and June together, with January wrapping one arm around June as they're covered with a bedsheet."
    elif relationship_type == "friendship":
        January "And that's why I'll always find a way to save you, June."
        June "And for that, I am forever grateful."
        "June and January go to January's home, following which they have a sleepover party."
        January "{i}Growing up, I'd felt so alone. So isolated. I thought nobody would ever understand me, or see the world the same way I did. But June does. My friendship with her means more than any victory I've tasted in the other timelines.{/i}"
        "A panel shows January and June together in casual pajamas. January's lazing back on her bed while June is relaxing on the couch."
    
    June "Are you sure we should leave Graham alone, though? I still can't shake the feeling that he'll remain a loose end."
    January "You leave that matter to me, my love. I'll use my Enforcer 0, Campanella, to take care of him."
    June "But if you're using Campanella, then..."
    January "Yup, he's loyal, so he won't go off and do his own thing. I know it goes against the spirit of what Ouroboros is supposed to be, but if it means saving your life, then..."
    
    if relationship_type == "romance":
        "June cuts off January with a kiss."
    
    June "Thank you, January. I...I wish I could find a way to make it up to you."
    "January gives a playful smile."
    January "Hmm, maybe you can."
    "June smiles nervously."
    June "I'm not sure I like where this is going..."
    January "But my backlog is piled up so high, June. I just keep jumping from one project to another and never finish anything."
    January "If you really want to make it up to me, maybe you can take a break from your own work and become my manager for a change. I've seen Sarah's capabilities, she'll do an excellent job managing Davidson Solutions in your absence."
    June "But I like my job as CEO. It's so comfortable with you covering for me."
    January "I know, and I don't regret spoiling you one bit. But come on, June, this idea must excite you a little. Stepping into my domain, seeing how I live my life day to day, isn't this something you've been waiting for?"
    
    if relationship_type == "romance":
        "June smiles and kisses January."
        June "It is. You've got yourself a deal, honey. But don't think I'll go easy on you."
    elif relationship_type == "friendship":
        "June smiles warmly."
        June "It is. You've got yourself a deal, friendo. But don't think I'll go easy on you."
    
    January "Believe me, with the backlog my ADHD has racked up, I don't want you to."
    "June and January laugh warmly alongside each other as the scene fades to black. The time skips to next week, where they're both in the Grandmaster's chambers that have an ethereal background, as she begins her next mission."
    Grandmaster "The Zephyr artifact retrieval? Really? But that's such a simple and boring mission."
    June "And one that'll blow up in your face if you don't finish it on time. No excuses, January."
    January "{i}I guess I shouldn't be surprised at how well June's adjusted to her new role, given the way she's led Davidson Solutions all these years. And despite my grumbling, she and I both know I wouldn't want things any other way.{/i}"
    January "Fiiine, I'll initiate the timeline dive."
    "A panel shows January powering up the timeline generator computer interface as June looks on in admiration and awe."
    "As the Zephyr artifact mission map loads up, January's dialogue tag changes back to the Grandmaster and her expression changes from playful grouchiness to ice-cold confidence."
    Grandmaster "Now, which Enforcer should I use this time?"
    
    return