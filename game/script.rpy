# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define mc = Character("Raine")
define na = Character()
define le = Character("Leona")
define ju = Character("Juneau")

define lj = Character("Leona's journal", kind=nvl)
define rj = Character("Raine's journal", kind=nvl)

image logo = "gui/Star Filled-48.png"
label splashscreen:
    show logo with Dissolve(2.0)
    hide logo with Dissolve(1.0)

label main_menu:
    return

label start:
    $ quick_menu = False
    show screen starfield
    pause (2.0)
    call screen navigation_2 with Dissolve(2.0)
    $ quick_menu = False


    
    "Space."
    
    "The final frontier."

    "These are the voyages of the starship Enterprise."

    hide screen starfield
    show screen starfield_with_image

    "It's continuing mission, to explore strange new worlds."
    "To seek out new life, and new civilisations."
    return

    # This ends the game.

    return




