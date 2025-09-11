label sc_romance_climax:

    Morgan "{i}My future with Sarah is all I care about now, and this asshole's in the way! He will die tonight!{/i}"

    Morgan "{i}Agent Graham may have cut through June's footsoldiers with ease, but they weren't masters of time like I am.{/i}"
    Morgan "{i}There's no move of his I can't foresee. No tactic of his I can't outmatch.{/i}"

    Morgan "Time to die, Graham! This is for Sarah!"
    Sarah "Goodbye, you sanctimonious old man. You won't be missed."

    "Montage of Morgan fighting and defeating Graham."
    show Morgan_default at right with moveinleft
    hide Graham with dissolve


    Morgan "We did it... oh my God we did it, Sarah! We won!"

    Sarah "That's right! We won, my love! The world is ours!"
    "They heard a voice from behind"
    "{color=#9d00ff} You two did win. A shame I can't say that for myself. {/color}"

    Sarah "Huh? What are you talking about, June?"
    show Sarah at right with dissolve
    show June at left with moveinleft
    Sarah " Graham's dead, we're in the clear."

    June "It's the burdens of leadership, Sarah."
    June "I tried a gamble to get Graham out of hiding, and it let him straight to my headquarters."
    June "You were just a pawn in my plans, so nobody will care what happens to you."
    June "But as for me? You'll find that my clients are rather... unforgiving."
    "Suddenly Morgan heard the sound of glass breaking and we see that June get shot through the head"
    "June collapsed"
    show June:
        rotate 270
    with dissolve
    show Sarah at center with moveinright
    Sarah "What? No, June, NO!"

    June "Let this be a lesson to you both. If you play with fire... you're going to get burned."
    June "I made promises I couldn't keep, and this is the result..."

    Sarah "(crying) I'm sorry, June! I'm sorry I couldn't protect you! I promise I'll make it right!"

    June "(coughing) Don't repeat my mistakes, June... don't make a promise you can't keep..."
    June "I've used you for my ambitions all your life, sweet child... but now you need to live for yourself..."
    June "Find a new life..."

    Morgan "I'll protect her, June. I'll stay with her no matter what. You can rest easy now, okay?"

    June "Thank you, Morgan... please... make Sarah happy..."
    June "She deserves to be rewarded... for serving me so well..."

    Morgan "{i}It's heartbreaking to see Sarah's career culminate in such a tragedy.{/i}"
    Morgan "{i}Perhaps things were always going to end this way.{/i}"
    Morgan "{i}But she still got a chance to say goodbye. And she still has me to lean on.{/i}"
    Morgan "{i}I will protect her, no matter what.{/i}"
    Morgan "{i}She won't meet the same end as her master.{/i}"
    Morgan "{i}We're both going to get our happy endings, whatever it takes.{/i}"


    jump sc_romance_ending

    return


label sc_romance_ending:
    scene Beach 
    "transition, our couple is at the beach"
    show Morgan_default at center
    show Sarah at center
    Morgan "{i}And so, I start my new life with Sarah. {/i}"
    Morgan "I must say, you have excellent taste in beachfront property."

    Sarah "(snuggles up to Morgan) Why thank you! I'm glad you finally listened to my infinite wisdom and stopped insisting on renting stuff all the time."
    Sarah "We're filthy rich and we should act like it!"

    Morgan "(kisses Sarah) I couldn't agree with you more, my love. You've truly made me see the light."

    Morgan "{i}And, of course, our vibrant event planning business keeps the coffers full even when assassination work dries up.{/i}"
    Morgan "{i}I really underestimated the benefits of having a 'legitimate business' as a cover.{/i}"

    Sarah "As much as murder remains my number one passion, I have come to enjoy providing the people a good time every now and then."

    Morgan "So have I. People deserve to have a chance to let loose every now and then."
    Morgan "After all, who knows when a fun vacation" 
    Morgan "(smirks deviously) might become your last."

    Morgan "{i}And with that, June Davidson is avenged.{/i}"
    Morgan "{i}It took a great deal of patience for the two of us to discover the identities of the five LambdaCorp executives who ordered her death, but it was all worth it.{/i}"
    Morgan "{i}June's killers walked right into our luxurious trap, and now their bodies will be cleaned out with no one the wiser.{/i}"

    Sarah "Some dishes really are best served cold, aren't they?"

    Morgan "Indeed they are." 
    Morgan "(kisses Sarah) And some dishes are best sampled... in private."

    Sarah "Lead the way, darling."

    # Ending achieved
    "Assassin Route Good Ending (Romance) achieved"

    return