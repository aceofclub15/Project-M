default persistent.story_tree = {
    "start": {
        "name": "Start - Choice 1",
        "children": ["emergency", "discreet"],
        "unlocked": False,
        "label": "sc_hotel_entrance"
    },
    "emergency": {
        "name": "Emergency -> Fail",
        "children": [],
        "unlocked": False,
    },
    "discreet": {
        "name": "Discreet",
        "children": ["stop_graham", "record_graham"],
        "unlocked": False,
    },
    "stop_graham": {
        "name": "Stop Graham  -> Fail",
        "children": [],
        "unlocked": False,
    },

    "record_graham": {
        "name": "Record Graham",
        "children": ["she_kill", "she_impersonate"],
        "unlocked": False,
    },
    "she_kill": {
        "name": "She might kill -> Investigate the noise",
        "children": ["investigate"],
        "unlocked": False,
    },
    "she_impersonate": {
        "name": "She might impersonate -> Investigate the noise",
        "children": ["investigate"],
        "unlocked": False,
    },
    "investigate": {
        "name": "Investigate the noise",
        "children": ["drink_poison", "stop_sarah", "help_sarah"],
        "unlocked": False,
        "color": "#66ff66",
    },
    "drink_poison": {
        "name": "Drink the poison -> Fail",
        "children": [],
        "unlocked": False,
    },
    "stop_sarah": {
        "name": "Stop Sarah",
        "children": ["give_room", "dont_give_room"],
        "unlocked": False,
        "color": "#0099cc",
    },
    "give_room": {
        "name": "Give room number -> Fail",
        "children": [],
        "unlocked": False,
    },
    "dont_give_room": {
        "name": "Don't give room number -> Choice 3",
        "children": ["choice3"],
        "unlocked": False,
    },
    "choice3": {
        "name": "Any ideas?",
        "children": ["no_sense", "planned"],
        "unlocked": False,
        "color": "#0099cc",

    },
    "no_sense": {
        "name": "Doesn't make sense ",
        "children": ["vigilante_ending"],
        "unlocked": False,
    },
    "planned": {
        "name": "This was planned",
        "children": ["vigilante_ending","ace_ending"],
        "unlocked": False,
    },
    "ace_ending": {
        "name": "Ace Ending",
        "children": [],
        "unlocked": False,
        "color": "#ff6666",
    },
    "vigilante_ending": {
        "name": "Vigilante Ending",
        "children": [],
        "unlocked": False,
        "color": "#ff6666",
    },

    "help_sarah": {
        "name": "Help Sarah",
        "children": ["master_time","hope_shot"],
        "unlocked": False,
        "color": "#0099cc",

    },
    "hope_shot": {
        "name": "Hope -> Fail",
        "children": [],
        "unlocked": False,
    },
    "master_time": {
        "name": "Master time",
        "children": ["choice4"],
        "unlocked": False,

    },
    "choice4": {
        "name": "Master time",
        "children": ["pro", "romance"],
        "unlocked": False,
        "color": "#0099cc",
    },
    "romance": {
        "name": "Romance",
        "children": ["test_commit"],
        "unlocked": False,
    },
    "test_commit": {
        "name": "Test commitment",
        "children": ["commit_romance", "stop_romance"],
        "unlocked": False,
        "color": "#0099cc",
    },
    "commit_romance": {
        "name": "Commit Romance",
        "children": ["assassin5"],
        "unlocked": False,
    },
    "stop_romance": {
        "name": "Stop Romance -> Go Home",
        "children": ["go_home"],
        "unlocked": False,
    },
    "pro": {
        "name": "Keep it professional -> Go home",
        "children": ["go_home"],
        "unlocked": False,
    },
    "go_home": {
        "name": "Go Home -> Assassin Route 5",
        "children": ["assassin5"],
        "unlocked": False,
        "color": "#66ff66",
    },
    "assassin5": {
        "name": "Assassin Route 5",
        "children": ["bluff", "bend_time"],
        "unlocked": False,
        "color": "#66ff66",
    },
    "bluff": {
        "name": "Bluff -> Fail",
        "children": [],
        "unlocked": False,
    },
    "bend_time": {
        "name": "Bend Time -> Assassin Route 6",
        "children": ["assassin6"],
        "unlocked": False,
    },
    "assassin6": {
        "name": "Assassin Route 6",
        "children": ["romance_ending","assassin_ending"],
        "unlocked": False,
        "color": "#66ff66",
    },
    "romance_ending": {
        "name": "Romance Ending",
        "children": [],
        "unlocked": False,
        "color": "#ff6666",
    },
    "assassin_ending": {
        "name": "Assassin Ending",
        "children": [],
        "unlocked": False,
        "color": "#ff6666",
    },
}
