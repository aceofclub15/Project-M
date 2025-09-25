label finalcredits:
    stop music
    scene black

    show screen creditscreen(1)
    pause 10
    hide screen creditscreen with dissolve

    show screen creditscreen(2)
    pause 8
    hide screen creditscreen with dissolve

    show screen creditscreen(3)
    pause 8
    hide screen creditscreen with dissolve
    return

transform fade_in_delay(delay=0.0):
    alpha 0.0
    pause delay
    linear 1.0 alpha 1.0

default delay = 2

screen creditscreen(sc):
    ## Ensure that the game_menu screens can't be stopped
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()



    if (sc == 1):
        text "Dev Team":
            color "#ffbf00"
            size 100
            xalign 0.52
            yalign 0.1
            at fade_in_delay((delay - 0.5))
    
        text "Programmer": 
            color "#ffbf00"
            size 50
            xalign 0.23
            yalign 0.3
            at fade_in_delay(delay)
        text "aceofclub":
            color "#00ae20"
            size 40
            xalign 0.24
            yalign 0.37
            at fade_in_delay(delay)

        text "Project Manager":
            color "#ffbf00"
            size 50
            xalign 0.5
            yalign 0.3
            at fade_in_delay((delay + 1))
        text "Genisys | Elliot":
            color "#061cdc"
            size 40
            xalign 0.5
            yalign 0.37
            at fade_in_delay((delay + 1))


        text "Writer":
            color "#ffbf00"
            size 50
            xalign 0.75
            yalign 0.3
            at fade_in_delay((delay + 2))

        text "MerCurious":
            color "#c5cc39"
            size 40
            xalign 0.75
            yalign 0.37
            at fade_in_delay((delay + 2))





        text "Artist":
            color "#ffbf00"
            size 50
            xalign 0.25
            yalign 0.6
            at fade_in_delay((delay + 3))

        text "Raiya":
            color "#770ed2"
            size 40
            xalign 0.25
            yalign 0.67
            at fade_in_delay((delay + 3))


        text "Music":
            color "#ffbf00"
            size 50
            xalign 0.5
            yalign 0.6
            at fade_in_delay((delay + 4))

        text "Platzy":
            color "#ee0f0f"
            size 40
            xalign 0.5
            yalign 0.67
            at fade_in_delay((delay + 4))


        text "Artist":
            color "#ffbf00"
            size 50
            xalign 0.75
            yalign 0.6
            at fade_in_delay((delay + 5))

        text "witchhunter666":
            color "#770ed2"
            size 40
            xalign 0.77
            yalign 0.67
            at fade_in_delay((delay + 5))


#SCREEN 2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    elif (sc == 2):
        text "Voice Actors":
            color "#ffbf00"
            size 100
            xalign 0.5
            yalign 0.1
            at fade_in_delay((delay - 0.5))

        text "Morgan": 
            color "#ffbf00"
            size 50
            xalign 0.25
            yalign 0.3
            at fade_in_delay(delay)
        text "Tabatha Tipton":
            color "#00bfff"
            size 40
            xalign 0.24
            yalign 0.37
            at fade_in_delay(delay)

        text "Sarah":
            color "#ffbf00"
            size 50
            xalign 0.5
            yalign 0.3
            at fade_in_delay(delay)
        text "Miko Phillips":
            color "#00bfff"
            size 40
            xalign 0.5
            yalign 0.37
            at fade_in_delay(delay)


        text "Graham":
            color "#ffbf00"
            size 50
            xalign 0.75
            yalign 0.3
            at fade_in_delay(delay)

        text "Garreth Bagwell":
            color "#00bfff"
            size 40
            xalign 0.8
            yalign 0.37
            at fade_in_delay(delay)


        text "Adam Roarke":
            color "#ffbf00"
            size 50
            xalign 0.20
            yalign 0.6
            at fade_in_delay((delay + 2))

        text "Austin Varvouletos":
            color "#00bfff"
            size 40
            xalign 0.19
            yalign 0.67
            at fade_in_delay((delay + 2))


        text "June":
            color "#ffbf00"
            size 50
            xalign 0.5
            yalign 0.6
            at fade_in_delay((delay + 2))

        text "Ren_Over_Shares":
            color "#00bfff"
            size 40
            xalign 0.5
            yalign 0.67
            at fade_in_delay((delay + 2))


        text "Grandmaster | January":
            color "#ffbf00"
            size 50
            xalign 0.85
            yalign 0.6
            at fade_in_delay((delay + 2))

        text "Hal Loomis":
            color "#00bfff"
            size 40
            xalign 0.78
            yalign 0.67
            at fade_in_delay((delay + 2)) 
    else:
        vbox:
            xalign 0.5   
            yalign 0.4  
            spacing 10   

            text "Special Thanks":
                color "#ffbf00"
                xalign 0.5
                size 50
                at fade_in_delay(delay)

            text "aceofclub":
                color "#00ae20"
                xalign 0.5
                size 45
                at fade_in_delay(delay + 0.5)
            text "for making the credits screen":
                color "#ffbf00"
                xalign 0.3
                size 40
                at fade_in_delay(delay+ 1.5)

