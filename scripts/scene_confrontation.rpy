label sc_confrontation:

    $ voice_line("m","hey","ang")
    Morgan "Hey! Hey, you! I'm hotel security."
    $ voice_line("m","grr","bad")
    Morgan "Just why were you trying to break into that room?!"
    show Morgan_default at left with moveinright
    show Graham at right with moveinbottom


    $ voice_line("g","huh","ang")
    Graham "(smiles viciously) Hotel security, huh?"
    $ voice_line("g","heh","ang")
    Graham "Awfully stupid of you to confront me without any backup, don't you think?"


    $ voice_line("m","hah","dis")
    Morgan "Don't push your luck, old man. Just answer my question!"

    "Graham shrugs"

    $ voice_line("g","tch","ang")
    Graham "You have no idea what you've gotten yourself into, kid. But I'm afraid your interference ends here. "
    $ voice_line("g","tch","bad")
    Graham "A pity, I never liked hurting women."
    "Graham dashes up to Morgan and injects Morgan with something before Morgan can react."
    $ voice_line("m","what","sur")
    Morgan "{i}What... what's going on... I can't feel my legs...? And my mind is fading..."
    $ voice_line("m","tch","ang")
    Morgan "{i}Oh wait, Graham stuck a needle in me... He tranquilized me before I knew it...{/i}"
    scene black
    $ voice_line("gm","so","bad")
    Grandmaster "{i}And so your mission comes to an undignified end, Morgan... Lying down on the floor, powerless to do anything.{/i}"
    Grandmaster "{i}You really should've remembered the first lesson I ever taught you. Never pick a fight you can't win.{/i}"
    Grandmaster "{i}Of course, Graham didn't heed the lesson either.{/i}"
    Grandmaster "{i}After knocking you out, he tried to face off against the assassin directly... And they both killed each other.{/i}"
    $ voice_line("gm","hmmph","bad")
    Grandmaster "{i}Do better next time.{/i}"

    "..."
    hide Graham
    jump sc_guest_list

    return
