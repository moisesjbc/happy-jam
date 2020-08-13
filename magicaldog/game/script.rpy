define jacob = Character('Jacob', color="#ffffff")
define hannah = Character('Hannah', color="#ffc8c8")
define marcos = Character('Marcos', color="#c8ffc8")
define lara = Character('Lara', color="#c8c8ff")

init:
    $ basic_dialogue_last_night_excuse = "Where were you last night at 10 PM?"
    $ basic_dialogue_last_night_notice_something = "Did you see or hear something strange last night at 10 PM?"
    $ basic_dialogue_throw_ball = "Throw ball and see if something magic happens"
    $ basic_dialogue_woof = "Mmmm... woof?"
    $ basic_dialogue_search_clues = "Search for clues"
    $ basic_dialogue_exit = "Bye"

label start:
    # TODO: Remove
    jump hannah

    show bg intro
    "Hi!"
    "My name is Jacob. I'm 20"
    "A year ago I won a world record eating the highest number of sandwiches in my garage"
    "It hurted and I developed a \"sandwich-phobia\""
    "But I am rich now!"
    "Since then I live in a mansion with my three dogs"

    show hannah normal at left
    with dissolve
    "Hannah..."
    show marcos normal
    with dissolve
    "Marcos..."
    show lara normal at right
    with dissolve
    "...and Lara"

    "A few days ago I went into the kitchen and discovered something"
    # Cookies jar animation
    show bg kitchen
    show object cookies jar:
        # Move source: <https://lemmasoft.renai.us/forums/viewtopic.php?t=16842>
        xpos 900
        ypos 200
        linear 2.0 xpos 350 ypos 200
    pause 2.5
    jacob "What the..."
    show object cookies jar:
        linear 0.1 xpos 350 ypos 800
    pause 2.0

    "It seems that one of them is a magical dog"
    "...or maybe all of them!"
    "No one of them said anything"
    "But it's cool for me!"
    "They are good dogs and I respect their privacy"
    "..."
    "But yesterday in the night hapenned something..."
    "I checked the camera on my room and..."

    show bg bedroom
    show object golden sandwich:
        xpos 900
        ypos 200
        linear 3.0 xpos -400 ypos 200
    pause 3.0
    "My golden sandwich was stolen using magic!"
    "The prize for my heroism!"
    "My most precious possesion!"
    "My rock!"
    "*Sigh*"
    "That's it!"
    "I am going to discover the guilty, no matter what!"

label dog_selector_menu:
    scene bg intro

    "Who should I question now?"

    menu:
        "Obviously Hannah":
            jump hannah
        "Marcos, of course":
            jump marcos
        "Lara, Du'uh":
            jump lara

label marcos:
    scene bg marcos bedroom
    with dissolve

    show marcos normal
    with dissolve

    marcos "What's up?"
    jump dog_selector_menu

label lara:
    scene bg lara bedroom
    with dissolve

    show lara normal
    with dissolve

    lara "Hi!"
    jump dog_selector_menu
