init:
    # Clues seen
    default hannah_clue_record_seen = False
    default hannah_clue_photos_seen = False
    default hannah_clue_radio_seen = False

    # Clues investigated
    default hannah_clue_record_investigated = False

    # Other flags
    default hannah_ending = None
    default hannah_requires_dog_medal = False


label hannah:
    play music "audio/hannah_theme.ogg"
    scene bg hannah bedroom
    with dissolve

    show screen hannah_clue_record
    show screen hannah_clue_photos
    show screen hannah_clue_radio

    show hannah normal
    with dissolve

    hannah "Hello, sir!"

label hannah_dialogue_menu:
    menu:
        "\"[basic_dialogue_last_night_excuse!t]\"":
            jacob "[basic_dialogue_last_night_excuse!t]"
            hannah "It was bed time, sir, so obviously I was here"

        "\"[basic_dialogue_last_night_notice_something!t]\"":
            jacob "[basic_dialogue_last_night_notice_something!t]"
            hannah "In fact I did, sir"
            hannah "I saw Lara burying something in the garden"
            "Mmm..."

        "[basic_dialogue_throw_ball!t]":
            "Suddenly I throw a toy ball to Hannah"
            hannah "!"
            hannah "What is the meaning of this, sir!"
            hannah "This is highly innapropiate for a superior!"
            hannah "For a dog, at least!"
            jacob "Sorry"
            "Maybe Hannah is not the one with magical powers?"

        "\"[basic_dialogue_woof!t]\"":
            jacob "[basic_dialogue_woof!t]"
            hannah "Lalilulelo"
            jacob "What?"
            hannah "Nothing"

        "[basic_dialogue_search_clues!t]":
            "Let's see what I find"
            jump hannah_clues

        "\"Can I check your security system?\"" if hannah_clue_record_seen and not hannah_clue_record_investigated:
            jacob "\"Can I check your security system?\""
            hannah "I am afraid not, sir!"
            jacob "What?"
            jacob "I thought that I was your superior"
            hannah "And you are, sir!"
            hannah "But this security system is personal"
            hannah "And according to law 1/359880/32 from the dog's code"
            $ hannah_requires_dog_medal = True
            hannah "A soldier can refuse to give a personal belonging to its superior (*)"
            hannah "(*) Except if the superior is a dog hero"
            jacob "I see"
            if "dog medal" not in inventory:
                "I could search the law on Internet and see what it takes to be a \"dog hero\""
                "But the only computer with Internet access in the house belongs to Marcos"
                $ hannah_about_being_dog_hero = True
            else:
                "I could show her my dog medal"
            "Or I just could scream \"A cat!\""
            "That would drive her crazy and set a distraction"
            "...but she may never forgive me"
            pause 1.0
            "What should I do?"

            menu:
                "\"Ok, never mind\"" if "dog medal" not in inventory:
                    jacob "Ok, never mind"

                "Show her the medal" if "dog medal" in inventory:
                    $ hannah_ending = "good"
                    "I show Hannah my dog medal"
                    "She inmediatly raises herself showing respect"
                    hannah "I didn't now, sir!"
                    hannah "Please, check my security system as you wish!"
                    jump investigate_hannah_record

                "\"Look! A cat!\"":
                    $ hannah_ending = "bad"
                    jacob "\"Look! A cat!\""
                    with hpunch
                    hannah "WHERE!"
                    "Hannah runs frenetically though the room, jumping and crying"
                    hannah "Where is it?!"
                    hannah "I need backup!"
                    hannah "Fire in the hole!"
                    hannah "grrrr"
                    "Ok, I got some time"
                    jump investigate_hannah_record

        "Talk with her about the security system log" if hannah_clue_record_investigated:
            jacob "According to the log on the security system..."
            hannah "Yes, sir?"
            jacob "Someone came by and you left the room with he or she"
            hannah "Impossible!"
            "Hannah checks the logs from the security system"
            "She looks surprise"
            hannah "This cannot be!"
            jacob "What do you mean?"
            jacob "Didn't you leave the room last night?"
            hannah "No, sir!"
            hannah "Something must be wrong with the system"
            hannah "I spent all the night here, as always!"
            "..."

        "Tell her that hannah saw her last night" if lara_saw_hannah:
            jacob "Hannah saw you last night..."
            jacob "Leaving my room"
            hannah "What...?"
            hannah "..."
            hannah "I trust Lara. She's a good soldier"
            hannah "If she saw me, then..."
            pause 1.0
            hannah "Maybe I am a sleepwalker?"
            jacob "And a sleepmagician?..."
            hannah "What?"
            jacob "Nothing!"
            hannah "What do the cameras on your room show, sir?"
            jacob "They..."
            "I don't want to mention the floating golden sandwich. Just in case"
            jacob "It's strange"
            jacob "They don't show you in my room"
            hannah "That's strange, sir"
            hannah "Maybe we have been hacked"
            hannah "Your cameras... my system..."
            "..."
            jacob "I'll investigate that"
            hannah "Me too, sir"

        "\"Why do you have photos of my golden sandwich?!\"" if hannah_clue_photos_seen:
            jacob "Why do you have photos of my golden sandwich?!"
            hannah "..."
            jacob "Answer me!"
            hannah "You didn't know where that prize came from, do you?"
            jacob "What do you mean?"
            hannah "It was made by cat artisans!"
            jacob "But..."
            hannah "YOU KNOW that I fought those creatures in the Great War between dogs and cats"
            hannah "How could you?"
            jacob "I didn't know. I am sorry!"
            hannah "..."
            jacob "But did you have to steal it?"
            hannah "What?"
            jacob "My golden sandwich dissapeared"
            hannah "I have nothing to do with that!"
            hannah "I would NEVER steal from a superior"
            hannah "Even if I hate that he has such a despicable possesion"
            jacob "But these photos..."
            hannah "*Sigh* I want dog artisans to build a replica of that thing"
            hannah "It was supposed to be a surprise..."
            jacob "Sorry..."
            jacob "I believe you"
            "... or do I?"

        "\"What is the radio for?\"" if hannah_clue_radio_seen:
            jacob "What is the radio for?"
            hannah "It's for notifying all the dogs in the neighborhour"
            hannah "In case of a cat attack"
            jacob "..."
            jacob "The war ended years ago"
            hannah "A soldier must be always prepared, sir"
            jacob "Yeah, but do you have to have like..."
            jacob "...a milion of them?"
            hannah "Yes!"
            jump hannah_dialogue_menu

        "\"Can I take one of your microphones?\"" if hannah_clue_radio_seen and marcos_requires_microphone and "microphone" not in inventory:
            jacob "\"Can I take one of your microphones?\""
            hannah "..."
            hannah "...."
            hannah "....."
            jacob "You have A LOT of them"
            hannah "Ok, ok"
            hannah "Here, sir!"
            $ inventory.append("microphone")
            show screen notify(message="Microphone added to then inventory")
            jacob "Thanks!"

        "\"[basic_dialogue_exit!t]\"":
            jacob "[basic_dialogue_exit!t]"
            hannah "Bye sir!"

            hide screen hannah_clue_record
            hide screen hannah_clue_photos
            hide screen hannah_clue_radio
            jump dog_selector_menu

    jump hannah_dialogue_menu

label investigate_hannah_record:
    "I check Hannah's security system"
    "What the...?"
    "According to the system, someone entered this room at 22:00"
    "Then two dogs left the room"
    "Later, Hannah entered again, alone"
    "..."
    $ hannah_clue_record_investigated = True
    jump hannah_dialogue_menu


# CLUE - Security system
###############################################################################

screen hannah_clue_record():
    # Source: <https://lemmasoft.renai.us/forums/viewtopic.php?t=19168>
    imagebutton:
        idle "images/object security system idle.png"
        hover "images/object security system hover.png"
        xpos 1000
        ypos 100
        if on_clues_screen and not seeing_clue:
            action Jump("hannah_clue_record_click")

label hannah_clue_record_click:
    $ seeing_clue = True
    $ hannah_clue_record_seen = True
    "This is a system for recording whenever someone enters or leaves Hannah's room"
    "Mmm..."
    "I could ask her about it"
    $ seeing_clue = False
    jump hannah_clues


# CLUE - Golden sandwich photos
###############################################################################

screen hannah_clue_photos():
    imagebutton:
        idle "images/object photos idle.png"
        hover "images/object photos hover.png"
        xpos 750
        ypos 350
        if on_clues_screen and not seeing_clue:
            action Jump("hannah_clue_photos_click")

label hannah_clue_photos_click:
    $ seeing_clue = True
    $ hannah_clue_photos_seen = True
    "These are..."
    "Photos of my golden sandwich!"
    "I must ask her about these!"
    $ seeing_clue = False
    jump hannah_clues


# CLUE - Radio
###############################################################################

screen hannah_clue_radio():
    imagebutton:
        idle "images/object radio idle.png"
        hover "images/object radio hover.png"
        xpos 50
        ypos 400
        if on_clues_screen and not seeing_clue:
            action Jump("hannah_clue_radio_click")

label hannah_clue_radio_click:
    $ seeing_clue = True
    $ hannah_clue_radio_seen = True
    "A radio?..."
    "...why?"
    $ seeing_clue = False
    jump hannah_clues


# CLUES screen
###############################################################################

label hannah_clues:
    show screen notify(message="Search possible clues and click on them to interact")
    $ on_clues_screen = True
    call screen clues_back_screen

    "Enough for now"
    jump hannah_dialogue_menu
