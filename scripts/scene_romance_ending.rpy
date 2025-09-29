# ROMANCE CLIMAX IN THE AP


label sc_romance_ending:
    scene bg beach
    show Morgan_default at left
    show Sarah at right
    $ voice_line("m","so","bad")
    Morgan "{i}And so, I start my new life with Sarah. {/i}"
    $ voice_line("m","well","hap")
    Morgan "I must say, you have excellent taste in beachfront property."
    $ voice_line("s","well","hap")
    Sarah "(snuggles up to Morgan) Why thank you! I'm glad you finally listened to my infinite wisdom and stopped insisting on renting stuff all the time."
    Sarah "We're filthy rich and we should act like it!"
    $ voice_line("m","yeah","hap")
    Morgan "(kisses Sarah) I couldn't agree with you more, my love. You've truly made me see the light."
    Morgan "{i}And, of course, our vibrant event planning business keeps the coffers full even when assassination work dries up.{/i}"
    Morgan "{i}I really underestimated the benefits of having a 'legitimate business' as a cover.{/i}"

    $ voice_line("s","so","hap")
    Sarah "As much as murder remains my number one passion, I have come to enjoy providing the people a good time every now and then."
    $ voice_line("m","so","hap")
    Morgan "So have I. People deserve to have a chance to let loose every now and then."
    $ voice_line("m","well","hap")
    Morgan "After all, who knows when a fun vacation" 
    Morgan "(smirks deviously) might become your last."
    $ voice_line("m","so","bad")
    Morgan "{i}And with that, June Davidson is avenged.{/i}"
    Morgan "{i}It took a great deal of patience for the two of us to discover the identities of the five LambdaCorp executives who ordered her death, but it was all worth it.{/i}"
    Morgan "{i}June's killers walked right into our luxurious trap, and now their bodies will be cleaned out with no one the wiser.{/i}"

    $ voice_line("s","well","bad")
    Sarah "Some dishes really are best served cold, aren't they?"
    $ voice_line("m","yes","hap")
    Morgan "Indeed they are." 
    Morgan "(kisses Sarah) And some dishes are best sampled... in private."
    $ voice_line("s","well","bad")
    Sarah "Lead the way, darling."

    # Ending achieved
    
    $ persistent.story_tree["romance_ending"]["unlocked"] = True
    $ persistent.romance_ending = True
    "Assassin Route Romance Ending achieved ([check_no_endings()]/4)"

    return