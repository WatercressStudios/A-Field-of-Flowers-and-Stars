##This block runs before the game starts up. It's mostly used to define objects such as images, characters, music etc.
init:

    ##Character Declarations: Creates character objects for each character in the game and assigns tags that will be used to reference their assets.
    define mc = Character("Raine", voice_tag = "mc", callback=speaker("mc"), what_color=colors.raine, image="mc")
    define le = Character("Leona", voice_tag="le", callback=speaker("le"), what_color=colors.leona, image="le")
    define ju = Character("Juneau", voice_tag="ju", callback=speaker("ju"), what_color=colors.ai, image="ju")
    ##These aren't seperate characters, but they're treated as such so we can give them their own properties.
    define lj = Character("Leona's journal", kind=nvl)
    define rj = Character("Raine's journal", kind=nvl)
    ##Does this blank one do anything?
    define na = Character()

    ##Style Properties
    ##Text Outlines: They take a value, a color, an x offset, and a y offset. The offsets are used if you want a drop shadow effect. Add more as needed.
    $ style.say_thought.outlines = [(0.2, "000000", 0, 0), (1, "#CCCCCC", 0, 0)]
    $ style.say_dialogue.outlines = [(0.2, "FFFFFF", 0, 0), (1, "#CCCCCC", 0, 0)]
    $ style.pref_label_text.outlines = [(0.2, "000000", 0, 0), (1, "#CCCCCC", 0, 0)]

    #This is the default transition used when changing from one expression to the next while the character is on screen. Doesn't affect when they enter or leave.
    define config.say_attribute_transition = dissolve

    ##Sprite offsets: Extra positions you can give to a sprite. Right now they are only xpos offsets but you can modify any part of the transform.
    ##You can use these to place a sprite "at leftoffset2"
    $ leftoffset = Position(xpos = .35)
    $ leftoffset2 = Position(xpos = .15)
    $ rightoffset = Position(xpos = .65)
    $ rightoffset2 = Position(xpos = .85)

    ##Transform Definitions: These are pre-defined animations we can call up so we don't have to code them every time.

    transform bounce:
    ##Makes a character slightly bounce when they pop into the scene. Gives them a bit of pep.
        yoffset 15
        easein .10 yoffset 0
        easeout .175 yoffset 15

    transform xflip:
    ##Used to flip a character to face the other direction.
        xzoom -1

    #Image Declarations: Image Tag = "file"
    ##Make sure the file names and extensions match, and that the files are in the correct directory. If there's image errors, check this section first.

    ##Logo images, stored in images/logos
    image watercresslogo = "logos/watercresslogo.png"
    image somnovalogo = "logos/somnovalogo.jpg"
    image sarchalenlogo = "logos/sarchalenlogo.png"
    image afofaslogo = "logos/afofaslogo.png"

    ##Sprite Definitions: The ones that are commented out are ones that don't look right.
    init python:
        layerorder = ['hair', 'base', 'arms', 'tail','mouth','eyes','brow',]
        DefineImages('images/sprites', composite=True, overrideLayerOrder=layerorder, offsets=(0, 100), zooms={'mc':0.4, 'le': 1.3, 'ju':1.3}, sides=['mc'])

        #Leona
        MapEmote('le curious', 'le think base tail_default mdo_default ed_default brow_default')
        MapEmote('le speaking a1', 'le neutral base arms_default mdo_default ed_default brow_default')
        MapEmote('le speaking a2', 'le neutral base arms_raised mdo_default ed_default brow_default')
        MapEmote('le questioning a1', 'le neutral base arms_default mdo_o ed_default brow_line')
        MapEmote('le questioning a2', 'le neutral base arms_raised mdo_o ed_default brow_line')
        MapEmote('le smug a2', 'le hip base arms_default tail_default mdo_smuggrin ed_default brow_default')
        MapEmote('le smug a1', 'le hip base arms_pout tail_default mdo_smuggrin ed_default brow_default')
        MapEmote('le smug a3', 'le hip base arms_raised tail_default mdo_smuggrin ed_default brow_default')
        MapEmote('le frustrated a1', 'le angry base arms_default mdo_default ed_default brow_default')
        MapEmote('le frustrated a2', 'le angry base arms_raised mdo_default ed_default brow_default')
        MapEmote('le sad', 'le sad base md_default ed_default brow_default')
        MapEmote('le happy a1', 'le neutral base arms_default md_default ed_default brow_default')
        MapEmote('le happy a2', 'le neutral base arms_raised md_default ed_default brow_default')
        MapEmote('le suspicious a2', 'le think base tail_default md_default ed_bedroom brow_default')
        MapEmote('le crying', 'le sad base md_default ed_sad brow_default')
        #MapEmote('le pout p1 1', 'le neutral base arms_default md_default ed_away brow_line')
        #MapEmote('le pout p1 2', 'le neutral base arms_raised md_default ed_away brow_line')


    ##background images, stored in images/backgrounds
    image white = "backgrounds/white.png"
    image stars = "backgrounds/stars.png"
    image cockpitoverlay = "overlays/cockpitoverlay.png"
    image cockpit_space = "backgrounds/cockpit_space.png"
    image cockpit_ground = "backgrounds/cockpit_ground.png"
    image cave = "backgrounds/cave.png"
    image street = "backgrounds/street.png"
    image spaceship_crashed = "backgrounds/spaceship_crashed.png"
    image house = "backgrounds/house.png"
    ##computer-graphics images, stored in images/cgs
    image cgTree = "cgs/cgtree.png"
    ##Sagi's stuff . Remove when it's no longer needed.
    image logo = "gui/Star Filled-48.png"
    image testbg = "gui/sagi/test/bg.jpg"
    # image side mc = "gui/sagi/test/raine.png"
    # image le = "gui/sagi/test/leona.png"

    ##Audio
    ##Channel for environment sound. This will allow audio for environmentals to be placed on it's own channel and levels for environmental effects to be adjusted with a fader
    $renpy.music.register_channel("env", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)


    ##**Note: Music and SFX will be referenced in-line and therefor don't need their own declarations**##


    ##Game updater. These are declarations used for the updater script to work. The important thing to know is that UPDATE URL
    ##points to a json file hosted online as an HTML accessable directory. When we build a new revision, Renpy will generate a few files used to update the game, including This
    ##json file. All of the files need to be uploaded to the webserver using cpanel or the command line and placed in this directory.

    ##Defines a URL where the .json file is hosted. It needs to be a public html with the compressed game files stored in the same directory.
    $ UPDATE_URL = "http://sarchalen.com/afieldofflowersandstars/update/updates.json"

init python:
    ##define VA info and parsing
    voices = {}
    voices['mc'] = '#Raine (VA Name)'
    voices['le'] = '#Leona (VA Name)'
    voices['ju'] = '#Juneau (VA Name)'
    # To do VA parsing after filling the above:
    # 1. Run the game in Ren'Py
    # 2. Call the console with 'shift+o'
    # 3. Type 'ParseVoices()' and hit enter

##This is our splash screen. It runs before the main menu and shows logos. It also requests game updates while the logos are showing (because of the delay it takes to contact the server)
label splashscreen:

    ##Used to check if a new version of the game exists. Returns a version number, or None.
    $ new_version = updater.UpdateVersion(url=UPDATE_URL, simulate=None)

    ##This sets default levels for audio channels in the prefs screen for the first time the player launches the game. It does nothing if the persistent file exists.
    python:
            if not persistent.set_volumes:
                persistent.set_volumes = True
                _preferences.volumes['music'] *= .3
                _preferences.volumes['voice'] *= .8
                _preferences.volumes['sfx'] *= .75

    ##Play the music configured in options so that the music begins as soon as the splash screen shows
    $ renpy.music.play(config.main_menu_music)

    scene black
    show afofaslogo at center with dissolve:
        zoom 0.3
        yanchor .5
        xpos .50
        ypos .45
    $ renpy.pause(2, hard=True)
    hide afofaslogo with dissolve

    ##When the splash screen ends, we jump to the updater script. If theres no updates, it will go to the menu screen and be invisible to the player.
    jump update

label update:
    ##If a new update exists, run the updater script located in the engine files at renpy/common/00updater.rpy
    ##**Note: Sarchalen uses a modified version of 00updater.rpy which integrates our GUI to create a seamless user experience.**##
    ##**If renpy is not using our game's GUI when the updater is run, you need to add this file to the renpy SDK before you create a build.**##
    ##**If anyone knows how to do this without modifying engine files please let us know :) **##

    if new_version != None:
        $ updater.update(url=UPDATE_URL, base=None, force=False, public_key=None, simulate=None, add=[], restart=True)
    else:
        return

label start:
    jump scene1
