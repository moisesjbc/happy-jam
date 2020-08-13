init:
    default hannah_clue_record_seen = False
    default hannah_clue_photos_seen = False
    default hannah_clue_radio_seen = False

label hannah:
    scene bg hannah bedroom
    with dissolve

    $ current_dog = "Hannah"

    show hannah normal
    with dissolve

    hannah "Hello, sir!"

label hannah_dialogue_menu:
    menu:
        "\"[basic_dialogue_last_night_excuse!t]\"":
            jacob "[basic_dialogue_last_night_excuse!t]"
            hannah "It was bed time, sir, so obviously I was here"
            jump hannah_dialogue_menu

        "\"[basic_dialogue_last_night_notice_something!t]\"":
            jacob "[basic_dialogue_last_night_notice_something!t]"
            hannah "In fact I did, sir"
            hannah "I saw Lara burrying something in the garden"
            "Mmm..."
            jump hannah_dialogue_menu

        "[basic_dialogue_throw_ball!t]":
            "Suddenly I throw a toy ball to [current_dog]"
            hannah "!"
            hannah "What is the meaning of this, sir!"
            hannah "This is highly innapropiate for a superior!"
            hannah "For a dog, at least!"
            jacob "Sorry"
            "Maybe [current_dog] is not the one with magical powers?"
            jump hannah_dialogue_menu

        "\"[basic_dialogue_woof!t]\"":
            jacob "[basic_dialogue_woof!t]"
            hannah "Lalilulelo"
            jacob "What?"
            hannah "Nothing"
            jump hannah_dialogue_menu

        "[basic_dialogue_search_clues!t]":
            "Let's see what I find"
            jump hannah_clues

        "\"Can I check your security system?\"" if hannah_clue_record_seen:
            jacob "\"Can I check your security system?\""
            hannah "Nope"
            jump hannah_dialogue_menu

        "\"Why do you have photos of my golden sandwich?!\"" if hannah_clue_photos_seen:
            jacob "Why do you have photos of my golden sandwich?!"
            hannah "..."
            jacob "Answer me!"
            hannah "You didn't know where that prize came from, do you?"
            jacob "What do you mean?"
            hannah "(Angry) It was made by cat artisans!"
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
            hannah "Even if I hate that he hast such a despicable possesion"
            jacob "But these photos..."
            hannah "*Sigh* I want dog artisans to build a replica of that thing"
            hannah "It was supposed to be a surprise..."
            jacob "Sorry..."
            jacob "I believe you"
            "... or do I?"
            jump hannah_dialogue_menu

        "\"What is the radio for?\"" if hannah_clue_photos_seen:
            jacob "What is the radio for?"
            hannah "It's for notifying all the dogs in the neighborhour"
            hannah "In case of a cat attack"
            jacob "..."
            jacob "The war ended years ago"
            hannah "A soldier must be always prepared, sir"
            jump hannah_dialogue_menu

        "\"[basic_dialogue_exit!t]\"":
            jacob "[basic_dialogue_exit!t]"
            hannah "Bye sir!"
            jump dog_selector_menu

    jump dog_selector_menu


# CLUE - Security system
###############################################################################

screen hannah_clue_record():
    # Source: <https://lemmasoft.renai.us/forums/viewtopic.php?t=19168>
    imagebutton:
        idle "images/object cookies jar.png"
        xpos 100
        ypos 100
        if not seeing_clue:
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
        idle "images/object cookies jar.png"
        xpos 400
        ypos 200
        if not seeing_clue:
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
        idle "images/object cookies jar.png"
        xpos 600
        ypos 200
        if not seeing_clue:
            action Jump("hannah_clue_radio_click")

label hannah_clue_radio_click:
    $ seeing_clue = True
    $ hannah_clue_photos_seen = True
    "A radio?..."
    "...why?"
    $ seeing_clue = False
    jump hannah_clues


# CLUES screen
###############################################################################

screen hannah_clues_screen():
    zorder 100
    frame:
        vbox:
            textbutton "Back" action Return()

label hannah_clues:
    show bg bedroom
    show screen notify(message="Search possible clues and click on them to interact")
    show screen hannah_clue_record
    show screen hannah_clue_photos
    show screen hannah_clue_radio
    call screen clues_back_screen

    hide screen hannah_clue_record
    hide screen hannah_clue_photos
    hide screen hannah_clue_radio

    "Enough for now"
    jump hannah_dialogue_menu
