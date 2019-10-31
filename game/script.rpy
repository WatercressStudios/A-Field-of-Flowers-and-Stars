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




# The game starts here.

# The game starts here.
label start:

    show screen starfield
    
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
