
define config.main_menu_music = "main_menu.wav"

init python:

    style.button.activate_sound = "button_sound.wav" 
    #background music channel for the main game
    renpy.music.register_channel("background")



    class start_with_sound(Action):
        def __init__(self, audio):
            self.audio = audio


        def __call__(self):
            renpy.play(self.audio)
            return Start()
