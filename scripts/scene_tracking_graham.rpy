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
    Sarah "Find anything?"
    $ voice_line("m","no","sad")
    Morgan "Nothing about his next move."
    Morgan "Though it looks like someone tipped Graham off about your job."
    Morgan "Someone you might know."

    Sarah "You mean Davidson Solutions?"

    $ voice_line("m","yeah","sad")
    Morgan "Yeah, looks like the job wasn't just about taking out Adam Rourke."
    Morgan "It was also about drawing Graham out of hiding."

    Sarah "What?! Christ, I've been wanting to settle things with Graham too, but for June to do this behind my back..."
    
    $ voice_line("m","what","ang")
    Morgan "June? Is she your boss?"

    Sarah "Yeah, June Davidson."
    Sarah "She's been really good to me for the most part, but sometimes she uses me like some kind of pawn!"
    Sarah "It pisses me off!"

    if romance:
        Morgan "(kisses Sarah) I'm sorry she treated you like that."
        Morgan "You deserve better than to be used as a tool."
        Morgan "I think you're amazing, just as you are."
        Sarah "Morgan... you mean it?"

        $ voice_line("m","yes","ang")
        Morgan "I do."
        Morgan "I promise you, no matter what Graham or June think of you, I'm going to put your needs first."
        Morgan "You can trust me, Sarah."
        Sarah "(kisses Morgan back) I do trust you. Thank you for being here, Morgan."
        Morgan "Anytime, Sarah."
        Morgan "Now, I haven't turned up anything on Graham's movements so far, but..."
    else:
        $ voice_line("m","well","bad")
        Morgan "In any case, it doesn't look like there's anything on Graham's movements here."

    Sarah "Maybe we should take a break, slow things down."
    Sarah "If we just take some time to think, then we might make a breakthrough."
    
    $ voice_line("m","yeah","sad")
    Morgan "Sounds good to me."

    Sarah "This is it! A map of the routes Graham is taking to uncover the truth behind Adam's murder."
    Sarah "It looks like he'll go to the Triplex Warehouse in Queens tomorrow night."
    
    $ voice_line("m","uh","bad")
    Morgan "Any idea where he is now?"

    Sarah "No, I can't piece it together from here."
    Sarah "But we finally have the jump on him, Morgan!"
    Sarah "When he arrives at the warehouse tomorrow, he won't know what hit him!"
    
    $ voice_line("m","good","dis")
    Morgan "Excellent, we know what to do now."

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
    Morgan "Do you want to take this chance to just... be with me for a while?"

    Sarah "(blushes) You mean, like, go out on a date?"

    $ voice_line("m","yes","ang")
    Morgan "Yes, something like that."

    Sarah "That sounds like a great idea."
    Sarah "I've been looking forward to spending some time with you too, Morgan."

    $ voice_line("m","uh","fea")
    Morgan "So um, what did you have in mind?"

    Sarah "Are you sure you don't want to take the initiative?"

    $ voice_line("m","no","sad")
    Morgan "Believe me, you don't want to put that pressure on me. My mind will just wanders from one place to another."
    Morgan "Without my master keeping me on track, I'd be a lost cause."

    Sarah "(giggles) Yeah, I know that feeling."
    Sarah "Well, lucky for you, I have a great idea in mind."
    Sarah "The MIX Gala's happening in a bit, and I can hack into the system and get two invites for us in a jiffy!"

    $ voice_line("m","oh","sur")
    Morgan "That's a fashion event, isn't it?"
    $ voice_line("m","uh","fea")
    Morgan "Are you sure I can pull it off?"

    Sarah "Are you kidding me?"
    Sarah "You looked amazing when I saw you back at the Charleston hotel!"

    default slay = ""
    python:
        if gender == "Male":
            slay = "King"
        else:
            slay = "Queen"

    Sarah "You've got this, [slay]!"

    $ voice_line("m","uh","bad")
    Morgan "Alright, if you say so. I guess I'll just go home and freshen up."
    
    Sarah "Indeed you will, darling."
    Sarah "And I'll send you the meetup coordinates and see you in an hour."
    Sarah "Don't keep me waiting."

    $ voice_line("m","hah","hap")
    Morgan "Wouldn't dream of it."

    Sarah "Oh and uh, once the date is over, maybe you can come over to my place and... stay there?"

    Sarah "I'm so excited about having my first time with a woman!"
    
    $ voice_line("m","right","hap")
    Morgan "Sarah, I thought you'd never ask."

    jump sc_motel
    return

label sc_motel:
    Morgan "{i}I really bet on the right horse while siding with Sarah.{/i}"
    Morgan "{i}I'm loving every second of this.{/i}"

    Sarah "Ah, there you are! Shall we go, my love?"

    Morgan "(kisses Sarah's hand) Indeed. After you, darling."

    "Scene transition. They go back to Sarah's place"
    scene black 
    show bg sarah_apartment with fade
    show Sarah at right
    show Morgan_default at left
    Morgan "I'm happy."

    Sarah "So am I, honey. So am I."

    $ voice_line("m","so","hap")
    Morgan "You remember what I told you, right? That you're amazing just as you are?"

    Sarah "You did. Now it's time for you to show me."


    jump sc_having_sex
    return


label sc_having_sex:
    scene black
    show bg sarah_apartment_dark
    Morgan "{i}And so I show her.{/i}"
    Morgan "{i}I show her how much she means to me, how much I love her.{/i}"
    Morgan "{i}And I make a vow to spend the rest of my life by her side, no matter what it takes.{/i}"
    Morgan "{i}This is a day I will never, ever forget.{/i}"

    Morgan "I had a wonderful time tonight. I... I love you, Sarah."

    Sarah "(kisses Morgan) I love you too."
    Sarah "And I share your vow."
    Sarah "We will spend the rest of our lives together, no matter what."

    $ voice_line("m","hah","hap")
    Morgan "I'm so, so happy to hear that."

    Sarah "There's just one more thing I need to do to make this official."
    Sarah "One final test for you before I accept you as my lifelong partner."

    Sarah "This is something I use for my daily meditation."
    Sarah "In order to revel in death, I need to know it, understand it."
    Sarah "If you drink this, you'll become just like me."
    Sarah "There will be nothing left between us."
    Sarah "Are you ready?"

    $ voice_line("m","yes","ang")
    Morgan "Of course I am."

    jump sc_drink_potion

    return


label sc_drink_potion:
    scene black
    show bg sarah_apartment
    show Morgan_default at center
    $ voice_line("m","uh","bad")
    Morgan "{i}I feel my senses leave me.{/i}"
    show DrK:
        xalign 0.5
        yalign 0.25
        zoom 0.5
    with fade
    Morgan "{i}It feels no different from being poisoned.{/i}"
    Morgan "{i}The void is coming for me, dragging me down into the abyss...{/i}"
    hide DrK with dissolve

    $ voice_line("gm","heh","hap")
    Grandmaster "You really should've known better than to fall in love with someone crazy, Morgan."
    Grandmaster "Getting together with an unrepentant murderer was only going to end one way, so..."
    with Pause(0.5)
    $ voice_line("gm","whoa","hap")
    Grandmaster "Oh wait, you're actually recovering, never mind."
    show Morgan_default at left with moveinright
    show Sarah at right with moveinright
    Sarah "(tearfully) Oh, thank God! Thank God you're okay!"

    $ voice_line("m","well","dis")
    Morgan "I told you, didn't I? My life belongs to you, now."
    Morgan "We'll be together, no matter what."

    Sarah "Yeah. Yeah, we will be."

    "Morgan falls asleep in Sarah's arms."

    jump sc_warehouse_trap

    return






#Professional have standars

label sc_separate_way:
    $ romance = False
    $ voice_line("m","no","ang")
    Morgan "Time to go our separate ways and prep."

    Sarah "Yeah, I suppose so."
    Sarah "But Morgan, you're a natural at this."
    Sarah "I really wish you'd found your way to our organization sooner."

    $ voice_line("m","well","hap")
    Morgan "I don't exactly disagree, but the Grandmaster has made good use of my talents so far."
    Morgan "I've had a pretty fortunate life already."

    Sarah "(smiles) I know you have."
    Sarah "And I owe Ouroboros a huge debt of gratitude for the help they've given me."
    Sarah "I'm just saying, if you truly commit to being an assassin like I am, you'll be unstoppable!"

    $ voice_line("m","well","bad")
    Morgan "I have crossed a number of lines already, but this is a big decision so I'll have to think about it."


    Sarah "Of course, Morgan, I don't mean to rush you."
    Sarah "I'm just putting all the cards on the table."
    Sarah "And in any case, you've already proven yourself to me."
    Sarah "Whoever I decide to kill next, it most assuredly won't be you."

    $ voice_line("m","uh","bad")
    Morgan "Uh... I'm happy to hear that."
    $ voice_line("m","so","ang")
    Morgan "Shall we go, then?"

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
    Morgan "{i}There isn't a lot to piece together about Graham beyond what me and Sarah have already dug up.{/i}"
    Morgan "{i}I guess if we want answers, we'll just have to get them from the man himself.{/i}"

    "Morgan let her mind wanders thinking about the Grandmaster"
    #"Morgan looks at the photo of GM and let his mind wanders"

    $ voice_line("m","well","bad")
    Morgan "{i}Is this truly the path you wanted me to take, Grandmaster?{/i}"
    Morgan "{i}I owe everything to you, and the last thing I want to do is let you down.{/i}"
    Morgan "{i}The unwavering faith you have in me has been so heartwarming, but it's also terrifying.{/i}"
    $ voice_line("m","sigh","bad")
    Morgan "{i}How can I ever repay you for saving my life when I was nothing?{/i}"

    jump sc_morgan_past
    return

label sc_morgan_past: 
    "Flashback time."
    scene black # Morgan_past
    show Young_Morgan:
        zoom 0.7
        xalign 0.2
        yalign 0.8
    Young_Morgan "Go away. I don't need your pity."
    show January at right
    $ voice_line("gm","well","sur")
    Grandmaster "Then consider yourself fortunate that I have none to offer."
    Grandmaster "I came to you because I see potential."
    Grandmaster "If you want to change your circumstances, you can come with me."
    Grandmaster "If you refuse, I'll leave."
    $ voice_line("m","grr","bad")
    Young_Morgan "Potential? What potential could a wretch like me possibly have?!"
    Young_Morgan "Everyone around me thinks I'm nothing!"
    
    $ voice_line("gm","hmmph","fea")
    Grandmaster "Then what if I told you that you can surpass them?"
    Grandmaster "Humiliate them?"
    Grandmaster "You don't need the failures around you to drag you down any longer, child."
    Grandmaster "Together, you and I will build a wonderful life those losers will forever envy!"
    "..."
    scene black

    Morgan "{i}Those words were all I needed to hear to accept her offer.{/i}"
    Morgan "{i}And the Grandmaster proved true to her word.{/i}"
    Morgan "{i}She's given me a place to belong, a place where I no longer need to hide or sulk in shame.{/i}"
    Morgan "{i}And I will spend my whole life serving her, even if her only ask is that I follow my heart.{/i}"

    Morgan "{i} Time to go to sleep.{/i}"
    jump sc_warehouse_trap

    return
