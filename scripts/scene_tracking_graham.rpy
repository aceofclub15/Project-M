label sc_track_graham:
    scene black
    show bg graham_apartment
    "Morgan and Sarah ransack Graham's apartment, dressed in black coveralls."
    show Morgan_default at center with moveinbottom
    $ voice_line("m","hmm","dis")
    Morgan "{i}Sarah's handlers are really good.{/i}"
    $ voice_line("m","sigh","hap")
    Morgan "{i}It didn't take long for the bigshots at Davidson Solutions to uncover Graham's hideout, though sadly, his exact whereabouts are unknown.{/i}"
    $ voice_line("m","well","bad")
    Morgan "{i}Still, this is a good spot for an ambush if he does return, not to mention that we may be able to track his next movements if we're smart enough.{/i}"
    show Morgan_default at left with moveinright
   
    show Sarah at right with moveinright
    $ voice_line("s", "ah", "hap")
    Sarah "Find anything?"
    $ voice_line("m","no","sad")
    Morgan "Nothing about his next move. Though it looks like someone tipped Graham off about your job. Someone you might know."

    $ voice_line("s", "oh", "hap")
    Sarah "You mean Davidson Solutions?"

    $ voice_line("m","yeah","sad")
    Morgan "Yeah, looks like the job wasn't just about taking out Adam Rourke. It was also about drawing Graham out of hiding."

    $ voice_line("s", "hmmph", "ang")
    Sarah "What?! Christ, I've been wanting to settle things with Graham too, but for June to do this behind my back..."
    
    $ voice_line("m","huh","sur")
    Morgan "June? Is she your boss?"
    $ voice_line("s","yeah","ang")
    Sarah "Yeah, June Davidson. She's been really good to me for the most part, but sometimes she uses me like some kind of pawn! It pisses me off!"

    if romance:
        $ voice_line("m","well","hap")
        Morgan "(kisses Sarah) I'm sorry she treated you like that. You deserve better than to be used as a tool."
        Morgan "I think you're amazing, just as you are."
        $ voice_line("s","uh","hap")
        Sarah "Morgan... you mean it?"
        $ voice_line("m","yes","hap")
        Morgan "I do. I promise you, no matter what Graham or June think of you, I'm going to put your needs first."
        Morgan "You can trust me, Sarah."
        $ voice_line("s","yeah","hap")
        Sarah "(kisses Morgan) I do trust you. Thank you for being here, Morgan."
        $ voice_line("m","well","hap")
        Morgan "Anytime, Sarah. Now, I haven't turned up anything on Graham's movements so far, but..."
    else:
        $ voice_line("m","so","bad")
        Morgan "In any case, it doesn't look like there's anything on Graham's movements here."
    $ voice_line("s", "so", "bad")
    Sarah "Maybe we should take a break, slow things down. If we just take some time to think, then we might make a breakthrough."
    $ voice_line("m","good","hap")
    Morgan "Sounds good to me."
    $ voice_line("s", "oh", "hap")
    Sarah "This is it! A map of the routes Graham is taking to uncover the truth behind Adam's murder."
    $ voice_line("s", "so", "hap")
    Sarah "It looks like he'll go to the Hallex Warehouse in Queens tomorrow night."
    $ voice_line("m","hmm","sad")
    Morgan "Any idea where he is now?"
    $ voice_line("s","no","ang")
    Sarah "No, I can't piece it together from here. But we finally have the jump on him, Morgan!"
    Sarah "When he arrives at the warehouse tomorrow, he won't know what hit him!"
    $ voice_line("m","good","hap")
    Morgan "Excellent, we know what to do now."
    $ voice_line("s", "so", "bad")
    Sarah "Exactly. So, what do you suggest we do next?"
    $ voice_line("m","hmm","bad")
    if romance:
        $ persistent.story_tree["test_commit"]["unlocked"] = True

        menu:
            "Maybe we use this time to get to know each other? (Go on date)":
                $ persistent.story_tree["commit_romance"]["unlocked"] = True
                jump sc_ask_date
            "We go our separate ways and prepare. (Keep it professional)":
                $ persistent.story_tree["stop_romance"]["unlocked"] = True
                jump sc_separate_way
    jump sc_separate_way
    
    return



#ROMANCE TIME

label sc_ask_date:
    $ voice_line("m","so","hap")
    Morgan "Do you want to take this chance to just...be with me for a while?"
    $ voice_line("s","uh","hap")
    Sarah "You mean, like, go out on a date?"
    $ voice_line("m","yeah","sad")
    Morgan "Yeah, something like that."
    $ voice_line("s","yeah","hap")
    Sarah "That sounds like a great idea. I've been looking forward to spending some time with you too, Morgan."
    $ voice_line("m","so","hap")
    Morgan "So um, what did you have in mind?"
    $ voice_line("s", "so", "hap")
    Sarah "Are you sure you don't want to take the initiative?"
    $ voice_line("m","sigh","sad")
    Morgan "Believe me, you don't want to put that pressure on me. My mind just wanders from one place to another."
    Morgan "Without my master keeping me on track, I'd be a lost cause."
    $ voice_line("s","yeah","hap")
    Sarah "Yeah, I know that feeling. Well, lucky for you, I have a great idea in mind."
    Sarah "The MIX Gala's happening in a bit, and I can hack into the system and get two invites for us in a jiffy!"
    $ voice_line("m","what","sur")
    Morgan "That's a fashion event, isn't it? Are you sure I can pull it off?"
    $ voice_line("s", "yeah", "hap")
    Sarah "Are you kidding me? You looked amazing when I saw you back at the Charleston hotel!"
    Sarah "You've got this, Queen!"
    $ voice_line("m","hmm","sad")
    Morgan "Alright, if you say so. I guess I'll just go home and freshen up."
    $ voice_line("s", "uh", "hap")
    Sarah "Indeed you will, darling. And I'll send you the meetup coordinates and see you in an hour."
    Sarah "Don't keep me waiting."

    $ voice_line("m","yeah","hap")
    Morgan "Wouldn't dream of it."
    $ voice_line("s","oh","hap")
    Sarah "Oh and uh, once the date is over, maybe you can come over to my place and... stay there? I'm so excited about having my first time with a woman!"
    $ voice_line("m","yes","hap")
    Morgan "Sarah, I thought you'd never ask."
    jump sc_motel
    return

label sc_motel:
    Morgan "{i}I really bet on the right horse while siding with Sarah. I'm loving every second of this.{/i}"


    $ voice_line("s","ah","hap")
    Sarah "Ah, there you are! Shall we go, my love?"
    $ voice_line("m","yeah","hap")
    Morgan "Indeed. After you, darling."
    "They go back to Sarah's aparment."
    scene black 
    show bg sarah_apartment with fade
    show Sarah at right
    show Morgan_default at left
    $ voice_line("m","so","hap")
    Morgan "I'm happy."
    $ voice_line("s","so","hap")
    Sarah "So am I, honey. So am I."
    $ voice_line("m","well","hap")
    Morgan "You remember what I told you, right? That you're amazing just as you are?"
    $ voice_line("s","yeah","hap")
    Sarah "You did. Now it's time for you to show me."
    jump sc_having_sex
    return


label sc_having_sex:
    scene black
    show bg sarah_apartment_dark
    $ voice_line("m","so","hap")
    Morgan "{i}And so I show her. I show her how much she means to me, how much I love her.{/i}"
    Morgan "{i}And I make a vow to spend the rest of my life by her side, no matter what it takes.{/i}"
    Morgan "{i}This is a day I will never, ever forget.{/i}"
    show bg bed_ms with dissolve
    $ voice_line("m","yeah","hap")
    Morgan "I had a wonderful time tonight. I... I love you, Sarah."
    $ voice_line("s","so","hap")
    Sarah "I love you too. And I share your vow. We will spend the rest of our lives together, no matter what."
    $ voice_line("m","good","hap")
    Morgan "I'm so, so happy to hear that."
    $ voice_line("s", "well", "hap")
    Sarah "There's just one more thing I need to do to make this official. One final test for you before I accept you as my lifelong partner."
    $ voice_line("s","so","bad")
    Sarah "This is something I use for my daily meditation. In order to revel in death, I need to know it, understand it."
    Sarah "If you drink this, you'll become just like me. There will be nothing left between us. Are you ready?"
    $ voice_line("m","well","hap")
    Morgan "I told you, didn't I? My life belongs to you, now. We'll be together, no matter what."
    jump sc_drink_potion

    return


label sc_drink_potion:
    scene black
    show bg poisoned with dissolve
    $ voice_line("m","uh","bad")
    Morgan "{i}I feel my senses leave me.{/i}"
    Morgan "{i}It feels no different from being poisoned.{/i}"
    Morgan "{i}The void is coming for me, dragging me down into the abyss...{/i}"
    scene black
    $ voice_line("gm","hmmph","bad")
    Grandmaster "You really should've known better than to fall in love with someone crazy, Morgan."
    Grandmaster "Getting together with an unrepentant assassin was only going to end one way, so..."
    with Pause(0.5)
    $ voice_line("gm","whoa","fea")
    Grandmaster "Oh wait, you're actually recovering, never mind."
    show bg sarah_apartment
    show Morgan_default at left with moveinright
    show Sarah at right with moveinright
    $ voice_line("s","yeah","hap")
    Sarah "Oh, thank God! Thank God you're okay!"
    $ voice_line("m","well","hap")
    Morgan "I told you, didn't I? My life belongs to you now. We'll be together, no matter what."
    $ voice_line("s","yeah","hap")
    Sarah "Yeah. Yeah, we will be."

    "Morgan and Sarah fall asleep in each other arms."
    jump sc_warehouse_trap

    return






#Professional have standars

label sc_separate_way:
    $ romance = False
    $ voice_line("m","so","bad")
    Morgan "I know what you're thinking Sarah, but maybe we should just focus on the mission."
    $ voice_line("s","yeah","bad")
    Sarah "Wait, that's it? I thought we'd take this opportunity to spend some more time together."
    $ voice_line("m","well","hap")
    Morgan "I understand that. I thought of it too, but I don't think I'm ready to fully commit to you, Sarah. I'm sorry."
    $ voice_line("s","so","hap")
    Sarah "That's a shame, Morgan, but I understand. Even if we won't be lovers, I'm happy to call you my friend. I wish you'd come across our organization sooner."
    $ voice_line("m","hmm","sad")
    Morgan "This is a big decision, Sarah. I'll have to think about it."
    $ voice_line("s", "yeah", "hap")
    Sarah "Of course, Morgan, I don't mean to rush you. I'm just putting all the cards on the table. And in any case, you've already proven yourself to me. Whoever I decide to kill next, it most assuredly won't be you."
    $ voice_line("m","well","hap")
    Morgan "Well, I'm happy to hear that. Shall we go, then?"
    $ voice_line("s", "so", "hap")
    Sarah "Indeed. Looking forward to tomorrow, partner."
    jump sc_remember_past

    return

label sc_remember_past:
    scene black
    #Morgan's home
    $ persistent.story_tree["go_home"]["unlocked"] = True
    hide Sarah with dissolve
    hide Morgan_default with dissolve
    $ voice_line("m","hmm","sad")
    Morgan "{i}There isn't a lot to piece together about Graham beyond what me and Sarah have already dug up. I guess if we want answers, we'll just have to get them from the man himself.{/i}"

    "Morgan lets her mind wander thinking about the Grandmaster."
    #"Morgan looks at the photo of GM and let his mind wanders"

    $ voice_line("m","well","bad")
    Morgan "{i}Is this truly the path you wanted me to take, Grandmaster?{/i}"
    Morgan "{i}I owe everything to you, and the last thing I want to do is let you down.{/i}"
    Morgan "{i}The unwavering faith you had in me is so heartwarming, but it was also terrifying.{/i}"
    $ voice_line("m","sigh","bad")
    Morgan "{i}How can I ever repay you for saving my life when I was nothing?{/i}"

    jump sc_morgan_past
    return

label sc_morgan_past: 
    scene black with Fade(0.1, 1, 0.5, color="#fff")
    # Morgan_past
    show Young_Morgan:
        zoom 0.7
        xalign 0.2
        yalign 0.8
    $ voice_line("m","grr","bad")
    Young_Morgan "Go away. I don't need your pity."
    show January at right
    $ voice_line("gm","good","hap")
    Grandmaster "Then consider yourself fortunate that I have none to offer. I came to you because I see potential."
    Grandmaster "If you want to change your circumstances, you can come with me. If you refuse, I'll leave."
    $ voice_line("m","what","sur")
    Young_Morgan "Potential? What potental could a wretch like me possibly have?! Everyone around me thinks I'm nothing!"
    
    $ voice_line("gm","well","ang")
    Grandmaster "Then what if I told you that you can surpass them? Humiliate them? You don't need the failures around you to drag you down any longer, child."
    Grandmaster "Together, you and I will build a wonderful life those losers will forever envy!"
    "..."
    scene black with Fade(0.1, 1, 0.5, color="#fff")


    $ voice_line("m","yeah","hap")
    Morgan "{i}Those words were all I needed to hear to accept her offer. And the Grandmaster proved true to her word.{/i}"
    Morgan "{i}She's given me a place to belong, a place where I no longer need to hide or sulk in shame.{/i}"
    Morgan "{i}And I will spend my whole life serving her, even if her only ask is that I follow my heart.{/i}"

    Morgan "{i} Time to go to sleep.{/i}"
    jump sc_warehouse_trap

    return