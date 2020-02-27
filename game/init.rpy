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
    transform hologram:
        parallel:
            alpha 0.0
            easeout 0.25 alpha 1.0
            easeout 0.25 alpha 0.9
        parallel:
            additive 0.0
            easeout 0.25 additive 1.0
            easein_cubic 0.75 additive 0.0
    transform stage_right:
        xanchor .5
        yanchor 1
        zoom 1.21
        ypos 0
        xpos .75

    transform stage_left:
        xanchor .5
        yanchor 1
        zoom 1.21
        ypos 0
        xpos .25

    transform bounce:
    ##Makes a character slightly bounce when they pop into the scene. Gives them a bit of pep.
        easein .10 yoffset 0
        easeout .175 yoffset 15

    transform xflip:
    ##Used to flip a character to face the other direction.
        xzoom -1

    transform easeback_right:
        subpixel True xpos 1.15
        parallel:
            ease_back 1.0 xpos 0.75

    transform ju_side:
        xpos 0.67 ypos 577 xanchor 1.55 yanchor 1 xzoom -1.0 zoom 1.13 alpha .9

    transform le_side:
        xpos 0.67 ypos 577 xanchor 1.55 yanchor 1 xzoom -1.0 zoom 1.13 alpha 1.0

    transform shake:
        linear 0.1 xoffset -2 yoffset 2
        linear 0.1 xoffset 3 yoffset -3
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat
    transform shake2:
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 4 yoffset -4
        linear 0.1 xoffset 3 yoffset -4
        linear 0.1 xoffset -5 yoffset 6
        linear 0.1 xoffset 6 yoffset 7
        repeat

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
        DefineImages('images/sprites', composite=True, overrideLayerOrder=layerorder, offsets=(0, 100), zooms={'mc':0.5, 'le': 1.3, 'ju':1.3}, sides=['mc'])

        #Leona
        MapEmote('le curious', 'le think base tail_default mdo_default ed_default brow_default')
        MapEmote('le speaking a1', 'le neutral base arms_default mdo_default ed_default brow_default')
        MapEmote('le speaking a2', 'le neutral base arms_raised mdo_default ed_default brow_default')
        MapEmote('le speakingsurprised a1', 'le neutral base arms_default mdo_o ed_default brow_default')
        MapEmote('le speakingthink', 'le think base tail_default mdo_default ed_bedroom brow_down')
        MapEmote('le speakingtired', 'le neutral base arms_raised mdo_o ed_default brow_uparrow')
        MapEmote('le questioning a1', 'le neutral base arms_default mdo_o ed_default brow_line')
        MapEmote('le questioning a2', 'le neutral base arms_raised mdo_o ed_default brow_line')
        MapEmote('le questioning a3', 'le hip base arms_raised tail_default mdo_pout ed_wide brow_default')
        MapEmote('le questioning p2', 'le neutral base arms_raised mdo_o ed_default brow_default')
        MapEmote('le shylook', 'le neutral base arms_raised md_default ed_away brow_uparrow')
        MapEmote('le smug a2', 'le hip base arms_default tail_default mdo_smuggrin ed_default brow_default')
        MapEmote('le smug a1', 'le hip base arms_pout tail_default mdo_smuggrin ed_default brow_default')
        MapEmote('le smug a3', 'le hip base arms_raised tail_default mdo_smuggrin ed_default brow_default')
        MapEmote('le frustrated a1', 'le angry base arms_default mdo_default ed_default brow_default')
        MapEmote('le frustrated a2', 'le angry base arms_raised mdo_default ed_default brow_default')
        MapEmote('le sad', 'le sad base md_default ed_default brow_default')
        MapEmote('le happy a1', 'le neutral base arms_default md_default ed_default brow_default')
        MapEmote('le happy a2', 'le neutral base arms_raised md_default ed_default brow_default')
        MapEmote('le happy speaking a2', 'le hip base arms_pout tail_default mdo_default ec_default brow_up')
        MapEmote('le happy speaking a3', 'le hip base arms_raised tail_default mdo_default ed_default brow_up')
        MapEmote('le happy2 a1', 'le hip base arms_pout tail_default mdo_smuggrin ed_wide brow_up')
        MapEmote('le smirk a2', 'le hip base arms_pout tail_default md_default ec_default brow_default')
        MapEmote('le suspicious a2', 'le think base tail_default md_default ed_bedroom brow_default')
        MapEmote('le crying', 'le sad base md_default ed_sad brow_default')
        MapEmote('le crying2', 'le sad base md_default ed_sad brow_default')
        MapEmote('le cryingtalk', 'le sad base mdo_default ed_sad brow_default')
        MapEmote('le catching', 'le angry base arms_default md_default ed_default brow_default')
        MapEmote('le sassyquestioning', 'le hip base arms_default tail_default mdo_pout ed_default brow_up')
        MapEmote('le concerned', 'le sad base md_default ed_default brow_default')
        MapEmote('le concernedspeaking', 'le sad base mdo_default ed_default brow_default')
        MapEmote('le explaining', 'le hip base arms_raised tail_default mdo_pout ed_default brow_default')
        MapEmote('le crazy', 'le hip base arms_pout tail_default mdo_default ed_wide brow_downarrow')
        MapEmote('le surprised', 'le hip base arms_raised tail_default2 mdo_pout ed_wide brow_up')
        MapEmote('le kind a2', 'le neutral base arms_raised mdo_default ed_default brow_uparrow')
        MapEmote('le relaxed', 'le neutral base arms_default md_default ec_default brow_default')
        MapEmote('le look', 'le neutral base arms_default md_default ed_away brow_uparrow')
        MapEmote('le hmm', 'le hip base arms_pout tail_default md_pout ed_wide brow_up')
        MapEmote('le tired', 'le sad base mdo_default ec_default brow_default')
        #MapEmote('le pout p1 1', 'le neutral base arms_default md_default ed_away brow_line')
        #MapEmote('le pout p1 2', 'le neutral base arms_raised md_default ed_away brow_line')

        #juneau
        MapEmote('ju snarky a1', 'ju blue base arms_default mdo_O ed_slightlyclosed brow_raised')
        MapEmote('ju snarky a2', 'ju blue base arms_raised mdo_O ed_slightlyclosed brow_raised')
        MapEmote('ju concerned a1', 'ju blue base arms_default mdo_O ed_default brow_uparrow')
        MapEmote('ju concerned a2', 'ju blue base arms_raised mdo_O ed_default brow_uparrow')
        MapEmote('ju speaking eclosed', 'ju blue base arms_default mdo_O ec_default brow_raised')
        MapEmote('ju sarcastic a1 e2', 'ju blue base arms_default md_O ec_default brow_default')
        MapEmote('ju sarcastic a1 e1 b4', 'ju blue base arms_default mdo_line ed_default brow_uparrow')
        MapEmote('ju annoyed a1', 'ju blue base arms_default mdo_O ed_default brow_downarrow')
        MapEmote('ju annoyed a2', 'ju blue base arms_raised md_O ed_slightlyclosed brow_default')
        MapEmote('ju red concerned a1', 'ju red hair_default base arms_worried mdo_O ed_default brow_worried')
        MapEmote('ju red sorry a3', 'ju red hair_default base arms_worried md_default ed_default brow_worried')
        MapEmote('ju red worried a1', 'ju red hair_default base arms_default mdo_small ed_glitch brow_raised')
        MapEmote('ju red worried speaking', 'ju red hair_default base arms_default mdo_small ed_glitch brow_worried')
        MapEmote('ju red sassy', 'ju red hair_default base arms_default mdo_default ec_angry brow_default')
        #raine
        MapEmote('mc thankful', 'mc normal base mdo_default ed_default brow_sad')
        MapEmote('mc yawn', 'mc armraised base mdo_default ed_default')
        MapEmote('mc yawn2', 'mc armraised base mdo_default ed_squint')
        MapEmote('mc neutral', 'mc normal base md_default ed_default brow_up')
        MapEmote('mc questioning', 'mc normal base mdo_O ed_lookup brow_sad')
        MapEmote('mc questioning2', 'mc confident base mdo_O ed_lookaway brow_raised')
        MapEmote('mc surprised', 'mc confident base mdo_stretchO ed_default brow_raised')
        MapEmote('mc shocked armraised', 'mc armraised base mdo_default ed_shock')
        MapEmote('mc shocked m2', 'mc armraised base mdo_O ed_shock')
        MapEmote('mc unimpressed', 'mc normal base mdo_O ed_lookaway brow_dreamworks')
        MapEmote('mc speaking', 'mc normal base mdo_default ed_liddrop brow_up')
        MapEmote('mc annoyed', 'mc angry base mdo_default ed_default brow_default')
        MapEmote('mc upset', 'mc angry hands md_default ec_default brow_angry')
        MapEmote('mc stern', 'mc angry base md_default ed_default brow_default')
        MapEmote('mc amused', 'mc normal base mdo_line ed_lookaway brow_sad')
        MapEmote('mc happy', 'mc confident base md_default ed_default brow_default')
        MapEmote('mc blech', 'mc confident base mdo_stretchO ec_default brow_angry')
        MapEmote('mc onfire', 'mc confident base mdo_stretch ec_blocky brow_angry')
        MapEmote('mc satisfied', 'mc confident base md_default ec_default brow_default')
        MapEmote('mc sighing', 'mc normal base md_line ed_lookup brow_sad')
        MapEmote('mc grumpy', 'mc normal base md_line ed_squint brow_angry')
        MapEmote('mc weary', 'mc normal base md_default ed_liddrop brow_sad')
        MapEmote('mc wearyspeak', 'mc normal base mdo_default ed_liddrop brow_sad')
        MapEmote('mc concernspeak', 'mc confident base mdo_stretchO ed_default brow_sad')
        MapEmote('mc shyspeak', 'mc normal base mdo_default ed_lookaway brow_sad')

    ##background images, stored in images/backgrounds
    image white = "backgrounds/white.png"
    image stars = "backgrounds/stars.png"
    image cockpitoverlay = "overlays/cockpitoverlay.png"
    image cockpit_space = "backgrounds/cockpit_space.png"
    image cockpit_ground = "backgrounds/cockpit_ground.png"
    image cave = "backgrounds/cave.png"
    image street = "backgrounds/street.png"
    image street_open = "backgrounds/street_open_garage.png"
    image spaceship_crashed = "backgrounds/spaceship_crashed.png"
    image house = "backgrounds/house.png"
    image cafe = "backgrounds/cafe.png"
    ##computer-graphics images, stored in images/cgs
    image cgTree = "cgs/cgtree.png"
    ##Sagi's stuff . Remove when it's no longer needed.
    image logo = "gui/Star Filled-48.png"
    image testbg = "gui/sagi/test/bg.jpg"
    # image side mc = "gui/sagi/test/raine.png"
    # image le = "gui/sagi/test/leona.png"

    ##Audio
    ##Channel for environment sound and extra sfx channel. This will allow audio for environmentals to be placed on it's own channel and levels for environmental effects to be adjusted with a fader
    $renpy.music.register_channel("env", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)
    $renpy.music.register_channel("sound2", mixer="sfx", loop=False, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)
    $renpy.music.register_channel("sound3", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)
    $renpy.music.register_channel("sound4", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)
    $renpy.music.register_channel("sound5", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)
    ##**Note: Music and SFX will be referenced in-line and therefor don't need their own declarations**##


    ##Game updater. These are declarations used for the updater script to work. The important thing to know is that UPDATE URL
    ##points to a json file hosted online as an HTML accessable directory. When we build a new revision, Renpy will generate a few files used to update the game, including This
    ##json file. All of the files need to be uploaded to the webserver using cpanel or the command line and placed in this directory.

    ##Defines a URL where the .json file is hosted. It needs to be a public html with the compressed game files stored in the same directory.
    $ UPDATE_URL = "http://sarchalen.com/afieldofflowersandstars/update/updates.json"

init python:
    ##define VA info and parsing
    voicefile_template = 'voice/{filenum}-{labelname}-{filelinenum}.ogg'
    #
    # {filename} the script file name
    # {filenum} the number in the script file name
    # {labelname} the name of the current label
    # {charname} the character short name
    # {filelinenum} the line number in the file
    # {labellinenum} the line number in the label
    # {charlinenum} the line number for the character in the file
    # {charlabellinenum} the line number for the character in the label
    #

    voices = {}
    voices['mc'] = '#Raine (Nat)'
    voices['le'] = '#Leona (Dot)'
    voices['ju'] = '#Juneau (Lily)'
    # To do VA parsing after filling the above:
    # 1. Run the game in Ren'Py
    # 2. Call the console with 'shift+o'
    # 3. Type 'ParseVoices()' or 'ParseVoices(comment_out_if_missing=True)' and hit enter
    #
    # Use the 'comment_out_if_missing=True' version if you want the script to comment out
    # the line automatically if the VA file doesn't exist
    #

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

    #scene starfield
    scene stars at main_menu_bg_transform with Dissolve(2.0)
    show afofaslogo:
        alpha 0
        zoom 0.4
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        parallel:
            linear 2 alpha 1
        parallel:
            linear 6 zoom 0.3
    $ renpy.pause(3, hard=False)
    hide afofaslogo with Dissolve(1.0)
    #scene black with Dissolve(2.0)

    ##When the splash screen ends, we jump to the updater script. If theres no updates, it will go to the menu screen and be invisible to the player.
    #jump update

# label main_menu:
#     # $ main_menu = True
#     $ speed = 0.5
#     scene stars at main_menu_bg_transform with Dissolve(2.0)
#     $ speed = 1.0
#     # show screen main_menu
#     $ renpy.call_in_new_context("main_menu")

label update:
    ##If a new update exists, run the updater script located in the engine files at renpy/common/00updater.rpy
    ##**Note: Sarchalen uses a modified version of 00updater.rpy which integrates our GUI to create a seamless user experience.**##
    ##**If renpy is not using our game's GUI when the updater is run, you need to add this file to the renpy SDK before you create a build.**##
    ##**If anyone knows how to do this without modifying engine files please let us know :) **##

    if new_version != None:
        $ updater.update(url=UPDATE_URL, base=None, force=False, public_key=None, simulate=None, add=[], restart=True)
    else:
        return

# label main_menu:
#     $ main_menu = True
#     scene starfield with dissolve
#     pause (2.0)
#     call screen main_menu with Dissolve(2.0)

label start:
    jump scene1
