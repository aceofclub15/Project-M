
define activate_btn_sound = "audio/sfx/button_sound.wav" 
define start_game_sound = "audio/sfx/menu_play.wav"
define main_menu_music = "audio/music/main_menu.wav"
define main_game_music = "audio/music/bg.wav"
define muffled_gun_shot_sfx = "audio/sfx/muffled_gunshot.wav"


init python:

    style.button.activate_sound = activate_btn_sound
    #background music channel for the main game
    renpy.music.register_channel("background")



    class start_with_sound(Action):
        def __init__(self, audio):
            self.audio = audio


        def __call__(self):
            renpy.play(self.audio)
            return Start()
