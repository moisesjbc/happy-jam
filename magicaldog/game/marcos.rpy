init:
    default first_time = True
    default marcos_clue_computer_status = None
    default marcos_clue_golosines_seen = False
    default marcos_requires_microphone = False
    default marcos_has_new_microphone = False
    default marcos_ending = None


label marcos:
    scene bg marcos bedroom
    with dissolve

    show screen marcos_clue_computer
    show screen marcos_clue_golosines

    show marcos normal
    with dissolve

    if first_time:
        $ first_time = False
        jacob "Hi Marcos..."
        marcos "Shhhhh!"
        "Marcos signals the computer. He seems to be recording another of his videos"
        "I wait patiently while he finishes"
        marcos "Hi everyone!"
        marcos "Welcome to another video from \"Origami for dogs\""
        marcos "Today we will be doing a giraffe!"
        marcos "As usual, this is all we need!"
        "He puts a white paper on the table, between the camera and him"
        marcos "Ok, are you ready?"
        marcos "I'll give you a second"
        pause 1.0
        marcos "GGRGRGRGRGRGAFMAKGMFASKLGMSDALKFSDAMKL"
        marcos "fmdkamkfdsamklfdasfkmdsaklfdsa"
        marcos "<war cries in multiple languages>"
        marcos "mfadsfmkdsafdsamlkfdsa"
        marcos "FMSAKDSAKMLDSAMKLADS"
        pause 1.0
        marcos "And that's all!"
        "The paper is now a mess of paper strips and dog's drool"
        "I can't distinguish it from his other \"creations\""
        "... as usual"
        marcos "I hope you enjoyed the video of today"
        marcos "Til' the next one!"
        pause 1.0

        "Marcos switch off the camera and looks to me"

    marcos "What's up?"

label marcos_dialogue_menu:
    menu:
        "\"[basic_dialogue_last_night_excuse!t]\"":
            jacob "[basic_dialogue_last_night_excuse!t]"
            marcos "Huh?"
            marcos "I was preparing my special video for 1k subscriptors"
            jacob "Oh..."
            jacob "Congratulations!"
            marcos "Don't pretend that you are happy for me!"
            jacob "What?"
            jacob "Where did that come from?"
            marcos "One day"
            marcos "One day and you got 5k followers"
            marcos "I have been working my ass for years and now I am starting to take off"
            marcos "Wait and you'll see!"
            "So that's what happening"
            "Maybe it stole the golden sandwich out of jealousy?"
            jump marcos_dialogue_menu

        "\"[basic_dialogue_last_night_notice_something!t]\"":
            jacob "[basic_dialogue_last_night_notice_something!t]"
            marcos "Nope"
            pause 1.0
            marcos "Well..."
            marcos "I heard noise coming from the corridor"
            marcos "I opened the door and saw Hannah walking"
            marcos "...to your room"
            pause 1.0
            jacob "Hannah?"
            marcos "I know"
            "She never leaves her room after 10 PM..."
            jump marcos_dialogue_menu

        "[basic_dialogue_throw_ball!t]":
            "Suddenly I throw a toy ball to Marcos"
            "Marcos jumps and bites the ball in the air"
            marcos "mfkdsamfksdafmlksdamfks"
            marcos "GRRRRRRRRRRRR"
            marcos "mfkmfdalfffggggrrrrrr"
            marcos "Here you go"
            "He handle to me another mess of paper strips and dog's drool"
            jacob "This..."
            marcos "It's a dolphin"
            jacob "Oh"
            jacob "Thanks!"
            marcos "You're welcome"
            jump marcos_dialogue_menu

        "\"[basic_dialogue_woof!t]\"":
            jacob "[basic_dialogue_woof!t]"
            marcos "I agree. Literature clubs are so much more than meets the eye"
            jacob "What?"
            marcos "Nothing"
            jump marcos_dialogue_menu

        "[basic_dialogue_search_clues!t]":
            "Let's see what I find"
            jump marcos_clues

        "\"Can I check your computer?\"" if marcos_clue_computer_status == "seen":
            jacob "\"Can I check your computer?\""
            marcos "No way"
            jacob "Why?"
            marcos "I don't trust you"
            jacob "That hurts!"
            marcos "I know"
            marcos "But you never showed any insterest on my content"
            marcos "And I know that you are afraid that I could exceed your number of followers"
            marcos "You might sabotage me!"
            jacob "What?"
            jacob "No sense!"
            marcos "Maybe, but it's what I feel"
            jacob "*Sigh*"
            marcos "Anyways"
            marcos "Why do you want to check my computer?"
            jacob "It's a secret"
            marcos "..."
            marcos "That doesn't help"
            jacob "Good point"
            pause 1.0
            jacob "Is there anything I can do to prove that I have good intentions?"
            marcos "Well..."
            marcos "You could get me a new microphone"
            jacob "A microphone?"
            marcos "Yes, my micro is full of drool and it isn't working as good as before"
            marcos "Can you believe it?"
            jacob "I do"
            marcos "Oh"
            marcos "So there it is"
            marcos "Get me a microphone and you would have proven youself worthy"
            $ marcos_requires_microphone = True

            if "microphone" in inventory:
                "I could give him the microphone"
            else:
                "I could look for a microphone for him"
                "Where could I found one?"

            "Or I could simply threaten him to report his channel with any made up excuse"
            "YouDog! is an strict platform and would close his channel while they investigate it"
            "It would ruin his reputation temporary, though"
            "And he might never forgive me"

            "What should I do?"

            menu:
                "\"Ok, I'll look for that microphone\"" if "microphone" not in inventory:
                    jacob "\"Ok, I'll look for that microphone\""
                    marcos "Perfect!"

                "Give microphone to Marcos" if "microphone" in inventory:
                    "I give the microphone to Marcos"
                    $ inventory = filter(lambda x: x != "microphone", inventory)
                    show screen notify(message="Microphone removed from inventory")
                    marcos "Oh!"
                    marcos "Thank you so much, bro!"
                    marcos "You really want to help me with the channel!"
                    jacob "Sure"
                    marcos "Thanks!"
                    $ marcos_ending = True
                    jump check_marcos_computer

                "Threaten him to report his channel on YouDog!":
                    jacob "You know..."
                    jacob "If you don't allow me your computer"
                    jacob "I could report your YouDog! channel"
                    marcos "!"
                    marcos "You wouldn't dare!"
                    jacob "I don't know..."
                    jacob "You wanna bet?"
                    marcos "You..."
                    marcos "Ok, check it!"
                    $ marcos_ending = False
                    jump check_marcos_computer

        "\"Where did you got those golosines?\"" if marcos_clue_golosines_seen:
            jacob "Where did you got those golosines?"
            marcos "From my subscriptors!"
            marcos "They are awesome!"
            jump marcos_dialogue_menu

        "\"Can I get some golosines?\"" if marcos_clue_golosines_seen:
            jacob "Can I get some golosines?"
            marcos "I think that they are not safe for humans"
            marcos "But sure!"
            $ inventory.append("golosines")
            show screen notify(message="Golosines added to the inventory")
            jump marcos_dialogue_menu

        "Ask for the gap in its work last night" if marcos_clue_computer_status == "investigated":
            jacob "I checked your computer and..."
            marcos "Yes...?"
            jacob "There is a gap"
            jacob "You stopped working at 20:00"
            marcos "Oh yes"
            marcos "I had some rest"
            jacob "Oh"
            "Suspecting..."
            "But I can't prove that he is lying"

        "Ask for the \"The Magical Dog\" tab" if marcos_clue_computer_status == "investigated":
            jacob "I checked your computer and..."
            marcos "Yes...?"
            jacob "Out of curiosity"
            jacob "What is this page about?"
            jacob "\"The Magical Dog\""
            marcos "!"
            marcos "That's nothing"
            marcos "It's..."
            marcos "It's a tutorial for improving your SEO on YouDog!"
            marcos "I know, I know"
            marcos "That name is not very descriptive"
            marcos "Click bait!"
            jacob "Mmmm"
            jacob "Can I check it?"
            jacob "It has a captcha for dogs"
            marcos "..."
            marcos "No, sorry"
            marcos "I can't let you learn my secrets!"
            "Marcos laughes nervously"
            jacob "I see"
            "Mmm..."

        "Check law 1/359880/32 on Internet" if marcos_clue_computer_status == "investigated" and hannah_requires_dog_medal:
            jacob "Can I search something on your computer?"
            marcos "Sure!"
            "I search for law 1/359880/32 on Internet"
            "I got to a PDF with 200 pages"
            "*Sigh*"
            "I hope this is worth it"
            "I search in the document for an eternity until I finally find it"
            "\"A dog hero is a dog or any other being (NOT A CAT)..."
            "...that fights a cat and survives\""
            "So that's it"
            "..."
            pause 1.0
            "Doesn't the neighbour have a cat?"
            "Fight the neigbour's cat?"
            menu:
                "Yes!":
                    pass
                "Sure!":
                    pass
                "Of course!":
                    pass
            "I go to the neighbour's garden"
            "I spot the neighbour's cat there"
            "I come close, like a ninja"
            cat "MEEEEEOOOOOW"
            with hpunch
            "Oh my"
            "We was waiting for me!"
            with hpunch
            "Ouch!"
            with hpunch
            "Ahhhhggg"
            "Meeedic!"
            with hpunch
            "My arm!"
            cat "MEEEEOOOOOOOW"
            with hpunch
            "I run for my life"
            "I get to my garden, wondering if I died"
            jacob "What the...?"
            "In front of me there are a dog medal on the grass"
            "It has a note"
            "\"For the dog hero!\""
            "*Sigh*"
            "I get the medal and return to Marcos' bedroom"
            $ inventory.append("dog medal")
            show screen notify(message="Dog medal added to inventory")

        "\"[basic_dialogue_exit!t]\"":
            jacob "[basic_dialogue_exit!t]"
            marcos "Bye!"
            hide screen marcos_clue_computer
            hide screen marcos_clue_golosines
            jump dog_selector_menu

    jump marcos_dialogue_menu


label check_marcos_computer:
    $ marcos_clue_computer_status = "investigated"
    "I check Marcos' computer"
    "Mmm... there's a gap here!"
    "He stopped working on his new video at about 22:00!"
    "There is something else..."
    "There is a tab opened"
    "Called \"The magical dog!\""
    "I click on it"
    "Theres a captcha for dogs"
    "\"Which of these are dog asses\""
    "All I see are 9 black images"
    "*Sigh*"
    jump marcos_dialogue_menu


# CLUE - Computer
###############################################################################

screen marcos_clue_computer():
    # Source: <https://lemmasoft.renai.us/forums/viewtopic.php?t=19168>
    imagebutton:
        idle "images/object computer idle.png"
        hover "images/object computer hover.png"
        xpos 50
        ypos 350
        if on_clues_screen and not seeing_clue:
            action Jump("marcos_clue_computer_click")

label marcos_clue_computer_click:
    $ seeing_clue = True
    $ marcos_clue_computer_status = "seen"
    "Marcos is all the time on his computer"
    "Maybe I can check his history for yesterday at night"
    $ seeing_clue = False
    jump marcos_clues


# CLUE - Golosines
###############################################################################

screen marcos_clue_golosines():
    # Source: <https://lemmasoft.renai.us/forums/viewtopic.php?t=19168>
    imagebutton:
        idle "images/object cookies idle.png"
        hover "images/object cookies hover.png"
        xpos 900
        ypos 400
        if on_clues_screen and not seeing_clue:
            action Jump("marcos_clue_golosines_click")

label marcos_clue_golosines_click:
    $ seeing_clue = True
    $ marcos_clue_golosines_seen = True
    "Golosines?"
    "I didn't buy those..."
    $ seeing_clue = False
    jump marcos_clues


# CLUES screen
###############################################################################

label marcos_clues:
    show screen notify(message="Search possible clues and click on them to interact")
    $ on_clues_screen = True

    call screen clues_back_screen

    "Enough for now"
    jump marcos_dialogue_menu
