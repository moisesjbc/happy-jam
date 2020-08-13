init:
    default first_time = True
    default marcos_clue_computer_seen = False

label marcos:
    $ current_dog = "Marcos"

    scene bg marcos bedroom
    with dissolve

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
            "Suddenly I throw a toy ball to [current_dog]"
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

        "\"Can I check your computer?\"" if marcos_clue_computer_seen:
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
            "Where could I get a microphone?"
            jump marcos_dialogue_menu

        "\"[basic_dialogue_exit!t]\"":
            jacob "[basic_dialogue_exit!t]"
            marcos "Bye!"
            jump dog_selector_menu

    jump dog_selector_menu


# CLUE - Computer
###############################################################################

screen marcos_clue_computer():
    # Source: <https://lemmasoft.renai.us/forums/viewtopic.php?t=19168>
    imagebutton:
        idle "images/object cookies jar.png"
        xpos 100
        ypos 100
        if not seeing_clue:
            action Jump("marcos_clue_computer_click")

label marcos_clue_computer_click:
    $ seeing_clue = True
    $ marcos_clue_computer_seen = True
    "Marcos is all the time on his computer"
    "Maybe I can check his history for yesterday at night"
    $ seeing_clue = False
    jump marcos_clues

# CLUES screen
###############################################################################

label marcos_clues:
    show screen notify(message="Search possible clues and click on them to interact")
    show screen marcos_clue_computer
    call screen clues_back_screen

    hide screen marcos_clue_computer

    "Enough for now"
    jump marcos_dialogue_menu
