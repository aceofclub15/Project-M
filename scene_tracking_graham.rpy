label sc_track_graham:
    scene somewhere
    "the next day? some time has passed? I'm not sure here."
    show Morgan_default at center with moveinbottom
    Morgan "{i}Sarah's handlers are really good.{/i}"
    Morgan "{i}It didn't take long for the bigshots at Davidson Solutions to uncover Graham's hideout, though sadly his exact whereabouts are unknown.{/i}"
    Morgan "{i}Still, this is a good spot for an ambush if he does return, not to mention that we may be able to track his next movements if we're smart enough.{/i}"
    show Morgan_default at left with moveinright
    show Sarah at right with moveinright
    Sarah "Find anything?"

    Morgan "Nothing about his next move."
    Morgan "Though it looks like someone tipped Graham off about your job."
    Morgan "Someone you might know."

    Sarah "You mean Davidson Solutions?"

    Morgan "Yeah, looks like the job wasn't just about taking out Adam Rourke."
    Morgan "It was also about drawing Graham out of hiding."

    Sarah "What?! Christ, I've been wanting to settle things with Graham too, but for June to do this behind my back..."

    Morgan "June? Is she your boss?"

    Sarah "Yeah, June Davidson."
    Sarah "She's been really good to me for the most part, but sometimes she uses me like some kind of pawn!"
    Sarah "It pisses me off!"

    if romance:
        Morgan "(kisses Sarah) I'm sorry she treated you like that."
        Morgan "You deserve better than to be used as a tool."
        Morgan "I think you're amazing, just as you are."
        Sarah "Morgan... you mean it?"
        Morgan "I do."
        Morgan "I promise you, no matter what Graham or June think of you, I'm going to put your needs first."
        Morgan "You can trust me, Sarah."
        Sarah "(kisses Morgan back) I do trust you. Thank you for being here, Morgan."
        Morgan "Anytime, Sarah."
        Morgan "Now, I haven't turned up anything on Graham's movements so far, but..."
    else:
        Morgan "In any case, it doesn't look like there's anything on Graham's movements here."

    Sarah "Maybe we should take a break, slow things down."
    Sarah "If we just take some time to think, then we might make a breakthrough."

    Morgan "Sounds good to me."

    Sarah "This is it! A map of the routes Graham is taking to uncover the truth behind Adam's murder."
    Sarah "It looks like he'll go to the Triplex Warehouse in Queens tomorrow night."

    Morgan "Any idea where he is now?"

    Sarah "No, I can't piece it together from here."
    Sarah "But we finally have the jump on him, Morgan!"
    Sarah "When he arrives at the warehouse tomorrow, he won't know what hit him!"

    Morgan "Excellent, we know what to do now."

    Sarah "Exactly. So, what do you suggest we do next?"

    if romance:
        Morgan "Maybe we use this time to get to know each other?"
        jump sc_ask_date
    else:
        Morgan "We go our separate ways and prepare."
        jump sc_separate_way
    return

label sc_separate_way:
    Morgan "It looks like we're done here. Time to go our separate ways and prep."

    Sarah "Yeah, I suppose so."
    Sarah "But Morgan, you're a natural at this."
    Sarah "I really wish you'd found your way to our organization sooner."

    Morgan "I don't exactly disagree, but the Grandmaster has made good use of my talents so far."
    Morgan "I've had a pretty fortunate life already."

    Sarah "(smiles) I know you have."
    Sarah "And I owe Ouroboros a huge debt of gratitude for the help they've given me."
    Sarah "I'm just saying, if you truly commit to being an assassin like I am, you'll be unstoppable!"

    Morgan "I have crossed a number of lines already, but this is a big decision."
    Morgan "I'll have to think about it."

    Sarah "Of course, Morgan, I don't mean to rush you."
    Sarah "I'm just putting all the cards on the table."
    Sarah "And in any case, you've already proven yourself to me."
    Sarah "Whoever I decide to kill next, it most assuredly won't be you."

    Morgan "Well, I'm happy to hear that."
    Morgan "Shall we go, then?"

    Sarah "Indeed. Looking forward to tomorrow, partner."

    jump sc_remember_past

    return

label sc_ask_date:
    Morgan "Do you want to take this chance to just... be with me for a while?"

    Sarah "(blushes) You mean, like, go out on a date?"

    Morgan "Yeah, something like that."

    Sarah "That sounds like a great idea."
    Sarah "I've been looking forward to spending some time with you too, Morgan."

    Morgan "So um, what did you have in mind?"

    Sarah "Are you sure you don't want to take the initiative?"

    Morgan "Believe me, you don't want to put that pressure on me."
    Morgan "My mind just wanders from one place to another."
    Morgan "Without my master keeping me on track, I'd be a lost cause."

    Sarah "(giggles) Yeah, I know that feeling."
    Sarah "Well, lucky for you, I have a great idea in mind."
    Sarah "The MIX Gala's happening in a bit, and I can hack into the system and get two invites for us in a jiffy!"

    Morgan "That's a fashion event, isn't it?"
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

    Morgan "Alright, if you say so."
    Morgan "I guess I'll just go home and freshen up."

    Sarah "Indeed you will, darling."
    Sarah "And I'll send you the meetup coordinates and see you in an hour."
    Sarah "Don't keep me waiting."

    Morgan "Wouldn't dream of it."

    Sarah "Oh and uh, once the date is over, maybe you can come over to my place and... stay there?"
    if gender == "Female":
        Sarah "I'm so excited about having my first time with a woman!"

    Morgan "Sarah, I thought you'd never ask."

    jump sc_motel
    return

label sc_motel:
    "Scene transition, some montage of them dating"
    Morgan "{i}I really bet on the right horse while siding with Sarah.{/i}"
    Morgan "{i}I'm loving every second of this.{/i}"

    Sarah "Ah, there you are! Shall we go, my love?"

    Morgan "(kisses Sarah's hand) Indeed. After you, darling."

    "Scene transition. They go back to Sarah's place"
    Morgan "I'm happy."

    Sarah "So am I, honey. So am I."

    Morgan "You remember what I told you, right? That you're amazing just as you are?"

    Sarah "You did. Now it's time for you to show me."


    jump sc_having_sex
    return


label sc_having_sex:
    Morgan "{i}And so I show her.{/i}"
    Morgan "{i}I show her how much she means to me, how much I love her.{/i}"
    Morgan "{i}And I make a vow to spend the rest of my life by her side, no matter what it takes.{/i}"
    Morgan "{i}This is a day I will never, ever forget.{/i}"

    Morgan "I had a wonderful time tonight. I... I love you, Sarah."

    Sarah "(kisses Morgan) I love you too."
    Sarah "And I share your vow."
    Sarah "We will spend the rest of our lives together, no matter what."

    Morgan "I'm so, so happy to hear that."

    Sarah "There's just one more thing I need to do to make this official."
    Sarah "One final test for you before I accept you as my lifelong partner."

    Sarah "This is something I use for my daily meditation."
    Sarah "In order to revel in death, I need to know it, understand it."
    Sarah "If you drink this, you'll become just like me."
    Sarah "There will be nothing left between us."
    Sarah "Are you ready?"

    Morgan "Of course I am."

    jump sc_drink_potion

    return
label sc_drink_potion:
    scene somewhere
    show Morgan_default at center
    Morgan "{i}I feel my senses leave me.{/i}"
    show DrK:
        xalign 0.5
        yalign 0.25
        zoom 0.5
    with fade
    Morgan "{i}It feels no different from being poisoned.{/i}"
    Morgan "{i}The void is coming for me, dragging me down into the abyss...{/i}"
    hide DrK with dissolve

    Grandmaster "Well, well, well. You really should've known better than to fall in love with someone crazy, Morgan."
    Grandmaster "Getting together with an unrepentant murderer was only going to end one way, so..."
    with Pause(0.5)
    Grandmaster "Oh wait, you're actually recovering, never mind."
    show Morgan_default at left with moveinright
    show Sarah at right with moveinright
    Sarah "(tearfully) Oh, thank God! Thank God you're okay!"

    Morgan "I told you, didn't I? My life belongs to you, now."
    Morgan "We'll be together, no matter what."

    Sarah "Yeah. Yeah, we will be."

    Morgan "Fall asleep in Sarah's arms."

    jump sc_warehouse_trap

    return


label sc_remember_past:
    hide Sarah with dissolve
    hide Morgan_default with dissolve
    Morgan "{i}There isn't a lot to piece together about Graham beyond what me and Sarah have already dug up.{/i}"
    Morgan "{i}I guess if we want answers, we'll just have to get them from the man himself.{/i}"

    Morgan "{i}Is this truly the path you wanted me to take, Grandmaster?{/i}"
    Morgan "{i}I owe everything to you, and the last thing I want to do is let you down.{/i}"
    Morgan "{i}The unwavering faith you have in me has been so heartwarming, but it's also terrifying.{/i}"
    Morgan "{i}How can I ever repay you for saving my life when I was nothing?{/i}"

    jump sc_morgan_past
    return

label sc_morgan_past:
    "Flashback time. (I don't know what to do here)"
    show Young_Morgan at left
    Young_Morgan "Go away. I don't need your pity."
    show GrandMaster at right
    Grandmaster "Then consider yourself fortunate that I have none to offer."
    Grandmaster "I came to you because I see potential."
    Grandmaster "If you want to change your circumstances, you can come with me."
    Grandmaster "If you refuse, I'll leave."
    Young_Morgan "Potential? What potential could a wretch like me possibly have?!"
    Young_Morgan "Everyone around me thinks I'm nothing!"

    Grandmaster "Then what if I told you that you can surpass them?"
    Grandmaster "Humiliate them?"
    Grandmaster "You don't need the failures around you to drag you down any longer, child."
    Grandmaster "Together, you and I will build a wonderful life those losers will forever envy!"
    "..."
    scene CurrentTime
    "transition. go back to current time"
    Morgan "{i}Those words were all I needed to hear to accept her offer.{/i}"
    Morgan "{i}And the Grandmaster proved true to her word.{/i}"
    Morgan "{i}She's given me a place to belong, a place where I no longer need to hide or sulk in shame.{/i}"
    Morgan "{i}And I will spend my whole life serving her, even if her only ask is that I follow my heart.{/i}"

    Morgan "{i} Time to fall asleep remembering the Grandmaster.{/i}"
    jump sc_warehouse_trap

    return
