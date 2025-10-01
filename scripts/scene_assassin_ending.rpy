#SC assassin climax in the AP



#SC assassin climax in the AP

label sc_assassin_ending:

    "Six months later."
    scene black  # random_warehouse
    show bg warehouse_interior
    Morgan "{i}Life has a way of surprising you.{/i}"
    Morgan "{i}I never thought I'd see Sarah again after our messy journey together, but I guess it must be a small world after all.{/i}"
    show Morgan_default at left
    show Sarah at right
    
    $ voice_line("s", "yeah", "sur")
    Sarah "Morgan? What are you doing here?"
    
    $ voice_line("m","well","hap")
    Morgan "Just another heist for the Grandmaster, stealing some intel on a planned merger between LambdaCorp and DarwinTech. What about you?"

    $ voice_line("s", "so", "hap")
    Sarah "I'm here on my own time. Trying to get some leads on who killed June."
    Sarah "LambdaCorp is a name that kept coming up in my research, so that's why I'm here."

    $ voice_line("m","yeah","sad")
    Morgan "I see. Well, I don't know if it'll help, but I could beam over a copy of the merger data I just swiped, in case you want to take a look at it."

    $ voice_line("s","oh","hap")
    Sarah "Wait, seriously? And the Grandmaster will just let you do that?"

    $ voice_line("m","well","hap")
    Morgan "What can I say? She gives her Enforcers a lot of discretionary power."

    $ voice_line("s", "so", "hap")
    Sarah "If I didn't know any better, I'd say you were taking me for a ride...but we have been through a lot together, haven't we?"

    $ voice_line("m","yeah","sad")
    Morgan "Yeah, we have."

    $ voice_line("s", "well", "hap")
    Sarah "Tell you what, you beam over the data, and I'll give you a map of my infiltration route."
    Sarah "I've cleaned out all the security on the way, so you'll have no problem making your exit."

    $ voice_line("m","well","dis")
    Morgan "Really? That'd be a big help, Sarah. You've got yourself a deal."

    $ voice_line("m","yeah","sad")
    Morgan "I guess I'll see you around, partner."
    
    $ voice_line("s", "well", "hap")
    Sarah "Until next time, then. Don't be a stranger."


    $ persistent.story_tree["assassin_ending"]["unlocked"] = True

    $ persistent.assassin_ending = True
    "Assassin Route Assassin Ending achieved ([check_no_endings()]/4)"
    jump finalcredits
    return