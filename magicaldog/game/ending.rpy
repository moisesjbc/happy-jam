
label ending:
    "So the moment has come"
    "I ask them all to come to the living room"
    scene bg living room
    with dissolve

    show hannah normal at left
    with dissolve

    show marcos normal
    with dissolve

    show lara normal at right
    with dissolve

    jacob "I have called all of you"
    jacob "Because something bad happened"
    jacob "My golden sandwich was stolen!"
    "I expected at least some emotion on their faces"
    "But no one of them seems to care a bit"
    "..."
    jacob "I have been collecting evidences"
    jacob "And I think I have a guilty"
    jacob "And the guilty is..."

    hide hannah
    with dissolve
    hide marcos
    with dissolve
    hide lara
    with dissolve

    menu:
        "\"Hannah!\"":
            pass
        "\"Marcos!\"":
            pass
        "\"Lara!\"":
            pass

    "I am about to say it"
    "But then..."

    show robert normal
    with dissolve

    jacob "What the...?"
    robert "Hi! My name is Robert!"
    robert "And welcome to my program \"The magical dog!\""
    "He proceeds to look directly to some invisible camera"
    robert "For those of you who doesn't know me"
    robert "I am a 30 years old dog!"
    robert "\"How is that?\" you might be wondering"
    robert "Well, 25 years ago I ate 55 lemons and I got superpowers!"
    robert "Since then, I travel through the world"
    robert "Sneaking in houses at checking the relation between humans and dogs!"
    robert "On this week's program"
    robert "I came to Jacob's house, as requested by one of his dogs, Marcos"
    "What?"
    if marcos_ending == "good":
        "Marcos smiles at me"
    else:
        "Marcos looks at me, serious"
    robert "Jacob leaves with his three dogs: Hannah, Marcos and Lara"
    robert "I came this house yesterday and set..."
    "Robert smiles at me"
    robert "and set a trap!"
    robert "I \"stole\" the \"golden sandwich\" from Jacob, his most precious belonging!"
    robert "I made sure that it would look for the guilty among his dogs"
    robert "But how would he find the evidences?"
    robert "Would he try to get all the info in a good, respectful way?"
    robert "Or would he abuse his powers to get to the truth?"
    robert "Let's find out with..."
    robert "Our dog jury!"
    robert "Remember, boys and girls"
    robert "Now it's your turn to judge your human with a \"good woof\" or a \"bad woof\"!"
    robert "So..."
    pause 1.0

    robert "Hannah?"
    hide robert
    with dissolve

    show hannah normal
    with dissolve
    hannah "Well..."
    if hannah_ending == "good":
        hannah "It's a \"good woof\" from me!"
        "Hannah smiles at me"
        hannah "He went so far as to fight a cat and get a medal for the truth!"
        hide hannah
        with dissolve
        show robert normal
        with dissolve
        robert "Wow!"
        robert "Awesome!"
    else:
        hannah "..."
        hannah "It's a \"bad woof\" from me!"
        "Hannah looks at me"
        hannah "Sorry, sir"
        "Hannah looks back at Robert"
        hannah "He pretended that there was a cat in my room!"
        hannah "Even knowing that that would traumatize me!"
        hide hannah
        with dissolve
        show robert normal
        with dissolve
        robert "That's bad!"
        robert "That's really bad!"
    pause 1.0

    robert "Ok"
    robert "What about you..."
    robert "...Marcos?"
    hide robert
    with dissolve
    show marcos normal
    with dissolve
    if marcos_ending == "good":
        marcos "It's a \"good woof\" from me!"
        "Marcos smiles at me"
        marcos "He gave me a new brand microphone!"
        marcos "Now I can keep given my YouDog! subscribers a top quality content and..."
        hide marcos
        with dissolve
        show robert normal
        with dissolve
        robert "Ok, ok, enough"
        "Robert smiles at Marcos"
        robert "That's sweet of him!"
    else:
        marcos "..."
        marcos "It's a \"bad woof\" from me!"
        "Marcos at me. He looks angry"
        marcos "It threatened me with reporting my YouDog! channel!"
        marcos "That could have mean the end for me!"
        marcos "And for my beloved subscribers, who are the best and..."
        hide marcos
        with dissolve
        show robert normal
        with dissolve
        robert "Ok, ok"
        pause 1.0
        robert "That's... not cool"
        "Robert looks at me"
    pause 1.0

    robert "And finally..."
    robert "What do you think..."
    robert "Lara?"
    hide robert
    with dissolve
    show lara normal
    with dissolve
    if lara_ending == "good":
        lara "It's a \"good woof\" from me!"
        "Lara smiles at me"
        lara "He never do any excersice since he won that damn golden sandwich!"
        lara "But he did it for retrieving my smart bracelet in a nice way!"
        hide lara
        with dissolve
        show robert normal
        with dissolve
        robert "Oh, that's cool!"
    else:
        lara "..."
        lara "It's a \"bad woof\" from me!"
        "Lara at me. She looks angry"
        lara "He offered me cookies!"
        robert "But that..."
        lara "I can't resist cookies!"
        lara "If I eat one I have to eat all of them!"
        lara "And then I forget about my training"
        lara "It was very difficult for me to get over my adiction!"
        hide lara
        with dissolve
        show robert normal
        with dissolve
        robert "Oh"
        robert "Now I understand"
        "Robert looks at me"
        robert "That was very mean of you, Jacob!"
    pause 1.0

    $ good_endings = len(filter(lambda e: e == "good", [hannah_ending, marcos_ending, lara_ending]))
    show robert normal
    with dissolve
    robert "Well, that's all"
    robert "The jury has spoken!"
    robert "We have... [good_endings] \"good woof\" out of 3!"
    robert "So..."
    pause 1.0

    if good_endings > 1:
        robert "You have proven yourself to be a good human!"
        robert "Congratulations!"
        robert "As a prize, you get to have your golden sandwich back!"
        robert "And you get the title of \"good human\"!"
        robert "Enjoy it!"
    else:
        robert "You have proven yourself to be a bad human!"
        robert "Your dogs certainly deserves better!"
        robert "As a punishment..."
        robert "You won't have you golden sandwich back!"
        robert "And you get the title of \"bad human\"!"
        robert "Anywhere you go, all dogs will know that you are not a friend of us!"
        robert "Shame on you!"

    "Robert looks directly to his invisible camera"
    robert "That's all for tonight's program, my dears!"
    robert "Stay tunned next week for a new program of..."
    robert "\"The magical dog!\""
    robert "Bye!"

    "Robert dissappears without saying anything else"
    hide robert
    with dissolve

    if good_endings > 1:
        "And I receive the approval and love of my beloved dogs!"
    else:
        "And I am left with three dogs that I treated bad!"
        "How can I live with this?"

    "THE END"
    "Made for the #1 Happy Jam on itch.io"
    return
