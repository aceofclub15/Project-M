default character_words = {
    "m": [
        "ah", "damn", "good", "grr", "hah", "hey", "hmm", "hmmph", "huh", "no",
        "oh", "really", "right", "shit", "sigh", "so", "tch", "thanks", "uh",
        "well", "what", "whoa", "yeah", "yes"
    ],
    "g": [
        "damn", "god", "grr", "hah", "haha", "heh", "hey", "hmmph", "huh", "no",
        "sigh", "so", "tch", "ugh", "wait", "well", "what", "whoa", "yeah", "yes"
    ],
    "gm": [
        "ah", "good", "heh", "hmmph", "okay", "so", "wait", "well", "whoa", "yes"
    ],
    "j": [
        "god", "grr", "haha", "heh", "hmm", "hmmph", "huh", "no", "oh", "right",
        "tch", "thanks", "uhh", "well", "yes"
    ],
    "r": [
        "good", "grr", "haha", "hmm", "huh", "no", "tch", "yeah", "yes"
    ],
    "s": [
        "ah", "damn", "god", "grr", "haha", "heh", "hey", "hmm", "hmmph", "huh",
        "no", "oh", "really", "shit", "sigh", "so", "tch", "uh", "well", "what",
        "whoa", "yeah", "yes"
    ]
}

default emotions = ["ang", "dis", "sad", "hap", "sur", "bad", "fea"]

init python:

    renpy.music.register_channel("channel_VAs", mixer="voice")
    renpy.music.set_volume(10, channel='channel_VAs')
    def voice_line(char, word, emo):
        filename = f"audio/voices/{char}_{word}_{emo}.wav"
        #renpy.play(filename,channel="channel_VAs")
        print(filename)
