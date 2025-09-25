
define activate_btn_sound = "audio/sfx/button_sound.wav" 
define start_game_sound = "audio/sfx/menu_play.wav"
define main_menu_music = "audio/music/main_menu.wav"
define music_bg_normal = "audio/music/bg_normal.wav"
define music_bg_action = "audio/music/bg_action.wav"



define sfx_muffled_gun_shot = "audio/sfx/muffled_gunshot.wav"
define sfx_tire_screech = "audio/sfx/tire_screech.wav"
define sfx_car_driving = "audio/sfx/car_driving.wav"
define sfx_car_leaving = "audio/sfx/car_leaving.mp3"

init python:

    style.button.activate_sound = activate_btn_sound
    #background music channel for the main game
    renpy.music.register_channel("channel_background", mixer="music")



    class start_with_sound(Action):
        def __init__(self, audio):
            self.audio = audio


        def __call__(self):
            renpy.play(self.audio)
            return Start()
