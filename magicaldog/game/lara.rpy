init:
    # Clues seen
    default lara_clue_smart_bracelet_seen = False

    # Clues investigated
    default lara_clue_smart_bracelet_investigated = False
    default lara_garden_investigated = False

    # Other flags
    default lara_ending = None
    default lara_saw_hannah = False


label lara:
    play music "audio/lara_theme.ogg"
    scene bg lara bedroom
    with dissolve

    if "bracelet" not in inventory:
        show screen lara_clue_smart_bracelet

    show lara normal
    with dissolve

    lara "Hello!"

label lara_dialogue_menu:
    menu:
        "\"[basic_dialogue_last_night_excuse!t]\"":
            jacob "[basic_dialogue_last_night_excuse!t]"
            lara "I was training at the garden."
            lara "As every night."
            jump lara_dialogue_menu

        "\"[basic_dialogue_last_night_notice_something!t]\"":
            jacob "[basic_dialogue_last_night_notice_something!t]"
            lara "..."
            lara "Not that I can remember now."
            jump lara_dialogue_menu

        "[basic_dialogue_throw_ball!t]":
            "Suddenly I throw a toy ball to Kara."
            "Lara jumps and bites the ball in the air."
            "Then she smiles at me."
            lara "Awesome! Again!"
            jacob "Maybe later."
            lara "Oh."
            "No magic here."
            jump lara_dialogue_menu

        "\"[basic_dialogue_woof!t]\"":
            jacob "[basic_dialogue_woof!t]"
            lara "Report mid."
            jacob "What?"
            lara "Nothing"
            jump lara_dialogue_menu

        "[basic_dialogue_search_clues!t]":
            "Let's see what I find."
            $ on_clues_screen = True
            jump lara_clues

        "\"Can I borrow your smart bracelet?\"" if lara_clue_smart_bracelet_seen and not lara_clue_smart_bracelet_investigated:
            jacob "Can I borrow your smart bracelet?"
            lara "Mmm."
            lara "Why do you want it?"
            jacob "Oh."
            jacob "For training, that's all!"
            lara "I don't know."
            lara "Since you won that damn golden sandwich you don't even train anymore."
            "She always blaims the world record for spoiling me."
            "Maybe she holds a grunt against it?"
            jacob "I know."
            jacob "But I want now."
            lara "Is that true?"
            jacob "Sure!"
            lara "Prove it!"
            jacob "How?"
            lara "Do some excercise with me."
            jacob "Now?"
            "Thinking about it makes me tired."
            "Maybe I really should do excercise every now and then."
            "Although..."
            "I could avoid doing excercise and instead offer her some dog cookies."
            if "cookies" not in inventory:
                "(I still need to find them, though)"
            "But she had a really bad adiction to cookies in the past."
            "And she may never forgive me..."

            "Would you do it?"
            menu:
                "\"Ok\" (Do excercise with her)":
                    jacob "Ok..."
                    jacob "What type of excercise?"
                    lara "Mmmm."
                    lara "Jumping."
                    lara "Yeah, that will do."
                    lara "Jump 5 times and I'll give you the bracelet."
                    "I think I am going to puke."
                    lara "Ready?"
                    jacob "Wait, I want to..."
                    lara "Now!"
                    with vpunch
                    "That hurts!"
                    lara "Good!"
                    jacob "I think I need some rest!"
                    lara "Again!"
                    with vpunch
                    "I think I am going to die here!"
                    jacob "Please!"
                    lara "Again!"
                    with vpunch
                    jacob "End this suffering!"
                    lara "Come on!"
                    jacob "Mercy!"
                    with vpunch
                    jacob "Tell my family I love them."
                    lara "And..."
                    jacob "I see a light."
                    lara "the..."
                    jacob "Should I come closer to it?"
                    lara "last one!"
                    with vpunch
                    jacob "I think that I died."
                    lara "Such a drama queen."
                    lara "Perfect!"
                    lara "Here."
                    lara "Take it."
                    jacob "Thanks."
                    lara "And Jacob."
                    jacob "Yes?"
                    lara "I hope that we could do excercise together more often!"
                    jacob "Sure!"
                    "I try hard not to let her see that I am crying in pain."
                    $ lara_ending = "good"
                    jump test_end

                "\"Maybe later\"" if "cookies" not in inventory:
                    lara "..."
                    lara "Ok"
                    jump lara_dialogue_menu

                "Buy her with cookies" if "cookies" in inventory:
                    jacob "Oh, what is this?"
                    "I take the cookies out of my pocket."
                    lara "Please no!"
                    with hpunch
                    "Lara jumps like a lightning and takes the cookies from my hands."
                    lara "I hate you!"
                    lara "grrgffgfdsg."
                    lara "Take it!"
                    $ lara_ending = "bad"
                    jump test_end

        "Ask her about her movements last night" if lara_clue_smart_bracelet_investigated and not lara_garden_investigated:
            jacob "Oh."
            lara "What is it?"
            jacob "Did you go to my room last night?"
            lara "!"
            lara "Yes, I did."
            jacob "Why?"
            lara "I heard some noises there."
            lara "I saw Hannah comming out."
            jacob "Did she say anything?"
            lara "No..."
            lara "She ignored me and walked back to her room."
            "Mmm..."
            $ lara_saw_hannah = True
            jacob "According to this you came back to the garden."
            lara "Sure, I resumed my training."
            jacob "What that training consisted of?"
            lara "Burying stuff."
            jacob "What kind of stuff?"
            lara "Bones!"
            lara "What else?"
            jacob "I see"

            "Should I confirm that?"
            menu:
                "Yes":
                    "I go to the garden and dig at the point marked by the smart bracelet."
                    "Oh my!"
                    "This cannot be!"
                    "I can't believe it!"
                    "It's..."
                    "It's..."
                    "A bone!"
                    "Lara yells at me from her window."
                    lara "Told you!"
                    lara "You better bury that again!"
                    jacob "Yes madam!"
                    "I bury the bone and return to Lara's room."
                    $ lara_garden_investigated = True
                "No":
                    "I decide to trust her."
            jump lara_dialogue_menu

        "\"[basic_dialogue_exit!t]\"":
            jacob "[basic_dialogue_exit!t]"
            lara "Bye bye!"
            hide screen lara_clue_smart_bracelet
            jump dog_selector_menu

    label test_end:
        $ lara_clue_smart_bracelet_investigated = True

        hide screen lara_clue_smart_bracelet
        $ inventory.append("bracelet")
        show screen notify(message="Smart bracelet added to inventory.")

        pause 1.0
        "Ok, so it's time to check the bracelet."
        pause 1.0
        "What the...?"
        "According to this, Lara went by my door last night."
        "Then she run to the garden..."
        jump lara_dialogue_menu

# CLUE - Smart bracelet
###############################################################################

screen lara_clue_smart_bracelet():
    imagebutton:
        idle "images/object bracelet idle.png"
        hover "images/object bracelet hover.png"
        xpos 900
        ypos 550
        if on_clues_screen and not seeing_clue:
            action Jump("lara_clue_smart_bracelet_click")

label lara_clue_smart_bracelet_click:
    $ seeing_clue = True
    $ lara_clue_smart_bracelet_seen = True
    "That bracelet of hers keep track of every move."
    "Maybe I can check her moves from last night."
    $ seeing_clue = False
    jump lara_clues

# CLUES screen
###############################################################################

label lara_clues:
    show screen notify(message="Search possible clues and click on them to interact.")
    call screen clues_back_screen

    "Enough for now"
    jump lara_dialogue_menu
