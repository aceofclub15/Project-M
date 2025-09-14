
define config.main_menu_music = "main_menu.wav"

init python:
    style.button.activate_sound = "button_sound.wav" 
    class start_with_sound(Action):
        def __init__(self, audio, pause_time = 0):
            self.audio = audio
            self.pause_time = pause_time

        def __call__(self):
            renpy.play(self.audio)
            return Start()
