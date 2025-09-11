label sc_confrontation:

    Morgan "Hey! Hey, you!"
    Morgan "I'm hotel security."
    Morgan "Just why were you trying to break into that room?!"
    show Morgan_default at left with moveinright
    show Graham at right with moveinbottom


    Graham "Hotel security, huh?"
    Graham "Awfully stupid of you to confront me alone, don't you think?"


    Morgan "Don't push your luck, old man."
    Morgan "Just answer my question!"

    Graham "You have no idea what you've gotten yourself into, kid."
    Graham "But I'm afraid your interference ends here."
    if gender == "Female":
        Graham "A pity, I never liked hurting women."

    Morgan "{i}What... what's going on...?"
    Morgan "{i}I can't feel my legs...{/i}"
    Morgan "{i}My mind is fading...{/i}"
    Morgan "{i}Oh wait, that's right...{/i}"
    Morgan "{i}Graham stuck a needle in me...{/i}"
    Morgan "{i}He tranquilized me before I knew it...{/i}"

    Grandmaster "{i}And so your mission comes to an undignified end, Morgan...{/i}"
    Grandmaster "{i}Lying down on the floor, powerless to do anything.{/i}"
    Grandmaster "{i}You really should've remembered the first lesson I ever taught you...{/i}"
    Grandmaster "{i}Never pick a fight you can't win.{/i}"
    Grandmaster "{i}Of course, Graham didn't heed the lesson either.{/i}"
    Grandmaster "{i}After knocking you out, he tried to face off against the assassin directly...{/i}"
    Grandmaster "{i}And they both killed each other.{/i}"
    Grandmaster "{i}Do better next time.{/i}"

    "..."
    hide Graham
    jump sc_guest_list

    return
