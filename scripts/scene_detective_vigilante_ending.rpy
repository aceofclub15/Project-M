label sc_obey_voice:
    scene bg hallex_warehouse
    show June at center zorder 5
    show Adam:
        rotate 270
        xalign 0.4
        yoffset 400

    show Graham at right
    show Graham:
        xoffset 100
        yoffset 200
        rotate 60
    show Sarah at right
    show Sarah:
        yoffset -100
        xoffset -100
    "Morgan drives to the Hallex warehouse. She finds a smug and self-assured June standing over Adam's dead body while Sarah is fighting a grieviously injured Graham."
    play sound sfx_tire_screech volume 1.5 fadeout 0.5
    pause 0.5
    $ voice_line("m","sigh","sad")
    Morgan "{i}I screwed up. I didn't do a good enough job at solving the Hallex case, and this is the result.{/i}"
    hide Adam
    show Morgan_default at left with moveinleft
    $ voice_line("j", "well", "hap")
    June "Agent Morgan, so good to finally meet you in person. Sarah's told me a lot about you."

    $ voice_line("m","oh","sur")
    Morgan "Oh, has she now?"
    $ voice_line("j", "right", "hap")
    June "Yes. How you're an annoyance. An impediment she can't seem to surpass."
    $ voice_line("j", "hmmph", "dis")
    June "It's no thanks to you, my little gamble almost didn't pay off. Which is why I had to come all the way here and settle things personally."
    $ voice_line("m","what","sur")
    Morgan "And what was your gamble, exactly?"
    $ voice_line("j", "hah", "bad")
    June "Oh Morgan, I'm not here to monologue my plan. I just wanted to show you the consequences of your failure."
    June "Because you weren't quick on your feet, the man you've been trying to save ended up dying anyway."
    "June points to Adam."
    $ voice_line("j", "well", "sad")
    June "And as for your partner in crime..."
    "June points to Sarah, who is sadistically smiling while strangling Graham to death."
    "Morgan rushes to try to defend Graham, but is pinned down by June."
    show Morgan_default at center with moveinleft
    hide June with dissolve
    hide Morgan_default with dissolve
    
    show June at center
    $ voice_line("j", "hah", "bad")
    June "Now now, agent. You'll get your turn. Now stay there and let the consequences of your failure sink in."
    "Sarah chokes Graham to death."
    hide Graham with dissolve
    $ voice_line("s", "yeah", "hap")
    Sarah "Yes, this is how I've wanted to end things with you Graham! I have ended you, while you cowered and realized you could NEVER surpass me!"
    "Suddenly Graham's slashes Sarah's throat with a switchblade"
    $ voice_line("s", "no", "ang")
    Sarah "Wha- URK!"
    show Graham at right
    show Graham:
        xoffset 100
        yoffset 200
    with dissolve
    $ voice_line("g","hah","hap")
    Graham "Hahahaha! I knew I was doomed the second you got the jump on me, Sarah. But I can at least take you down with me!"
    "Sarah collapses, bleeding to death. At the same time, Graham dies from his previous grevious injuries."
    hide Sarah
    hide Graham

    $ voice_line("j", "no", "fea")
    June "No! No, this can't be happening, I-"
    show Morgan_default:
        rotate 0
    show June at center
    show June:
        rotate 270
        yoffset 300
    "Morgan takes advantage of June's distraction to overpower her and hold her at gunpoint."
    $ voice_line("m","grr","bad")
    Morgan "I'm going to make you pay, June, for everything that you've done!"
    $ voice_line("j", "no", "fea")
    June "No! NO! I'd almost fixed everything! Now...he will...oh January, I'm so sorry!"
    $ voice_line("m","what","sur")
    Morgan "What are you talking about?"
    $ voice_line("j","grr","ang")
    June "I can't disappoint him, I can't let him know I failed! Even January can't save me now! I'M ENDING THIS!"
    "June tries to slash at Morgan with a pocket knife. Morgan shoots her dead in self-defense."
    hide June with dissolve
    "After that, Morgan searches the bodies, trying to find whatever clues she can."
    "In Adam's wallet, she finds a mysterious ID belonging to a man named Marcus Simms."
    $ voice_line("m","sigh","sad")
    Morgan "{i}This bloody spectacle before me reminds me of my failure. My inadequacy.{/i}"
    Morgan "{i} Graham died because I wasn't a good enough agent. But at the very least, I will avenge my fallen friend no matter what.{/i}"
    
    jump sc_vigilante_epilogue
    return


label sc_vigilante_epilogue:
    scene bg office

    "A year passes by. An elevator opens and Marcus Simms enters into his high-rise office."
    play sound sfx_elevator_ring volume 1.5 fadeout 0.5
    pause 1
    show Marcus at right with moveinleft
    "As he approaches his swivel chair, he hears Morgan's voice from behind."
    $ voice_line("m","hmm","dis")
    Morgan "I've read such glowing articles about you, Marcus. People respected you as one of the pre-eminent National Security Advisors in the United States."
    Morgan "A pity they didn't know you were just a double-crosser, selling state secrets."
    show Morgan_default at left with moveinleft
    "Marcus slowly tries to open his gun drawer without Morgan noticing."
    Marcus "Well, people can be naive. I just did what anyone else would in my position. Tell me, did you come alone?"
    $ voice_line("m","yes","ang")
    Morgan "I did. You need to answer for all the people who are dead because of you. June Davidson, Sarah, and my old friend, Graham."
    "Marcus pulls out his gun and fires at Morgan. The trigger clicks but the chamber is empty."
    $ voice_line("m","hah","ang")
    Morgan "You disappoint me, Marcus. I already took the bullets out of your gun. Surely, you should've foreseen that."
    Marcus "And what about you? Can you foresee the consequences of the path you're on? If you keep going down this road of vengeance and bloodshed, you may end up in a similar position to me one day."
    $ voice_line("m","hmm","bad")
    Morgan "I'll take my chances."
    play sound sfx_muffled_gun_shot volume 1.5 fadeout 0.5
    "Morgan shoots her silent pistol at Marcus, killing him."
    play sound sfx_elevator_ring volume 1.5 fadeout 0.5
    "Morgan leaves the office using the elevator."

    scene black

    $ persistent.story_tree["vigilante_ending"]["unlocked"] = True

    $ persistent.vigilante_ending = True
    "Detective route vigilante ending achieved ([check_no_endings()]/4)"
    jump finalcredits
    return