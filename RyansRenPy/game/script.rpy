# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene park2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show character at right

    # These display lines of dialogue.

    e "This is a Ren'Py game."

    e "It was coded with renpy."

    e "Testing this thing?"

    # This ends the game.

    menu:
        "The test worked":
            jump test_work
        "The test worked! Whoever coded this must be a genius.":
            jump test_also_work
    label test_work:
        "Thanks, I knew that, considering that the code got to this point."
        jump after_menu
    label test_also_work:
        "Yes, I agree."
        jump after_menu
    label after_menu:
#        "This happened after the menu, in case you care."
    return