label sc_obey_voice:
    scene hallex_warehouse
    "Morgan arrives alone at the Hallex warehouse, where she finds the smug and self-assured June and Sarah standing over a dead Adam and a grieviously injured Graham."
    show June at center
    show Adam:
        rotate 90
        xalign 0.8
        yalign 0
    show Graham at topright
    show Sarah at right
    Morgan "{i}I screwed up. I didn't do a good enough job at solving the Hallex case, and this is the result.{/i}"
    show Morgan_default at left with moveinleft
    June "Agent Morgan, so good to finally meet you in person. Sarah's told me a lot about you."

    Morgan "Oh, has she now?"
    June "Yes. How you're an annoyance. An impediment she can't seem to surpass."
    June "It's all thanks to you that my little gamble almost fell to pieces, which is why I had to come all the way here and settle things personally."
    Morgan "And what was your gamble, exactly?"
    June "Oh Morgan, I'm not here to monologue my plan. I just wanted to show you the consequences of your failure."
    June "Because you weren't quick on your feet, the man you've been trying to save ended up dying anyway."
    "June points to Adam with her thumb."
    June "And as for your partner in crime."
    "June gestures to Sarah, who smiles sadistically and begins to strangle Graham to death."
    "Morgan rushes to Graham's defense, only for June to pin her down and force her to watch."
    show Morgan_default at center with moveinleft
    hide June with dissolve
    show Morgan_default:
        rotate 270
    show June at center
    June "Now now, agent. You'll get your turn. Now stay there and let the consequences of your failure sink in."
    "Sarah chokes Graham to death, her smile vicious."
    Sarah "Yes, this is how I've wanted to end things with you, Graham! I'll end you, while you cower and realize you could NEVER surpass me! Hehehe, yes, YES!"
    "Sarah's expression grows increasingly ecstatic as the life goes out of Graham's eyes, when suddenly, he slashes her throat with a switchblade."
    Sarah "Wha- URK!"
    Graham "I knew I was doomed the second you got the jump on me, Sarah. But I could at least take you down with me! Hahahaha!"
    "Both Sarah and Graham bleed to death, Graham laughing like a madman all the while."
    show Sarah:
        rotate 90
    show Graham:
        rotate 90
    June "No! No, this can't be happening, I-"
    hide Morgan with dissolve
    show Morgan_default:
        rotate 0
    show June at center
    show June:
        rotate -290
        yoffset 80
    "Morgan takes advantage of June's distraction to overpower her and hold her at gunpoint."
    Morgan "I'm going to make you pay, June, for everything that you've done!"
    June "No! NO! I'd almost fixed everything! Now Wallace...he will..."
    Morgan "What are you talking about?"
    June "I can't disappoint him, I can't let him know I failed! I'D RATHER DIE!"
    "Suddenly, June slashes at Morgan with a pocket knife, causing Morgan to shoot her dead in self-defense."
    show June:
        rotate 90
    "After that, Morgan searches the everyone's body and try to find whatever clues she can."
    "She then notices a mysterious ID card belonging to a man named Marcus Simms in Adam's wallet."
    Morgan "{i}This bloody spectacle before me reminds me of my failure. {b}My inadequacy.{/b} {/i}"
    Morgan "{i} Graham died because I wasn't a good enough detective. But, at the very least, I will avenge my fallen friend, no matter what.{/i}"
    
    jump sc_vigilante_epilogue
    return


label sc_vigilante_epilogue:
    scene highrise_office
    "Time skips by one year. A high-rise office is shown. An elevator opens, and Marcus Simms enters the room."
    show Marcus at right with moveinleft
    "As he approaches his swivel chair, he hears Morgan's voice from behind."
    Morgan "I've read such glowing articles about you, Marcus. People respected you as one of the pre-eminent national security advisors in the United States. A pity they didn't know you were just a double-crosser selling state secrets."
    show Morgan_default at left with moveinleft
    "Marcus composes himself and tries to sneakily open his gun drawer."
    Marcus "Well, people can be naive. I just did what anyone else would in my position. Tell me, did you come alone?"
    Morgan "I did. You need to answer for all the people who are dead because of you. June Davidson, Sarah, and my old friend, Graham."
    "Marcus pulls out his gun and fires. But the chamber is empty."
    Morgan "You disappoint me, Marcus. I already took the bullets out of your gun. Surely, you should've foreseen that."
    Marcus "And what about you? Can you foresee the consequences of that path you're on? If you keep going down this road of vengeance and bloodshed, you may end up in a similar position to me one day."
    Morgan "I'll take my chances."
    "Morgan shoots Marcus dead with a silenced pistol and leaves."
    scene black
    "Detective route vigilante ending achieved"
    $ persistent.vigilante_ending = True
    return