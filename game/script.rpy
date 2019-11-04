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

label start:
    scene testbg with dissolve

    mc "Rather, here, everyone travels among the same streets, trodding upon the same dusty ground - where an alien like myself can find home among the pleasantries of the locals."

    show le with dissolve
    le "Space."

    le "The final frontier."

    ju "These are the voyages of the starship Enterprise."

    show starfield bigstars with dissolve

    "It's continuing mission, to explore strange new worlds."
    "To seek out new life, and new civilisations."

    # This ends the game.

    return
