# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define mc = Character("Raine", what_color=colors.raine, image="mc")
define na = Character()
define le = Character("Leona", what_color=colors.leona)
define ju = Character("Juneau", what_color=colors.ai)

define lj = Character("Leona's journal", kind=nvl)
define rj = Character("Raine's journal", kind=nvl)

image logo = "gui/Star Filled-48.png"

image testbg = "gui/sagi/test/bg.jpg"
image side mc = "gui/sagi/test/raine.png"
image le = "gui/sagi/test/leona.png"

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
    #$ quick_menu = False

    hide screen starfield with dissolve
    hide screen navigation_2 with dissolve

    scene testbg with dissolve

    mc "Rather, here, everyone travels among the same streets, trodding upon the same dusty ground - where an alien like myself can find home among the pleasantries of the locals."

    show le with dissolve
    le "Space."

    le "The final frontier."

    ju "These are the voyages of the starship Enterprise."

    show screen starfield_with_image

    "It's continuing mission, to explore strange new worlds."
    "To seek out new life, and new civilisations."
    return

    # This ends the game.

    return
