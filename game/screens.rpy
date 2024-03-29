﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")
    idle_background Frame('gui/sagi/button-idle.png', Borders(55, 0, 55, 0))
    insensitive_background Frame('gui/sagi/button-disabled.png', Borders(55, 0, 55, 0))
    hover_background Frame('gui/sagi/button-highlighted.png', Borders(55, 0, 55, 0))
    xysize (250, 107)

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/sagi/frame.png", gui.frame_borders)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                # id "namebox"
                # style "namebox"
                if who in colors.namebox:
                    background colors.namebox[who]
                else:
                    background colors.namebox['Default']
                xysize (225, 55)
                pos (182, -3)
                text who id "who":
                    xalign 0.5
                    text_align 0.5
                    color colors.base

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        if who == 'Raine':
            add SideImage() xalign -0.05 yalign 1.0
        elif not who in hide_sides:
            add SideImage() xalign 1.26 yalign -1.75

transform change_transform(old, new):
    contains:
        old
        xalign 0.08
        yalign 1.0
        yoffset 520
        easeout 0.2 yoffset 1080
    contains:
        new
        xalign 0.08
        yalign 1.0
        yoffset 1080
        easein 0.3 yoffset 500
        ease 0.1 yoffset 520

transform change_transform_static(old, new):
    contains:
        old
        yalign 1.0
        xpos 0.0 xanchor 0.0 xoffset 180
        ease 0.2 alpha 0
    contains:
        new
        yalign 1.0
        xpos 0.0 xanchor 0.0 xoffset 180
        alpha 0
        ease 0.2 alpha 1

transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)
    xpos 0.0 xanchor 0.0 xoffset 180

define config.side_image_change_transform = None
define config.side_image_same_transform = None


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign gui.textbox_xalign
    yalign gui.textbox_yalign
    xsize gui.textbox_width
    ysize gui.textbox_height

    background Frame("gui/sagi/textframe.png", Borders(72, 0, 72, 0), xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background colors.neutral
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

transform flower_menu_transform:
    anchor (0.5, 0.5)
    on show:
        zoom 0.0
        easein 0.15 zoom 1.02
        ease 0.05 zoom 1.0
    on hide:
        easein 0.2 zoom 0.0

transform flower_button_transform:
    on idle:
        linear 0.2 alpha 0.5
    on hover:
        linear 0.2 alpha 1

screen flower_menu_button():
    if quick_menu:
        # frame at flower_menu_transform:
        #     background None
        #     align (1.0, 0.0)
        #     offset (-110, 220)
        #     imagebutton at flower_button_transform:
        #         align (0.5, 0.5)
        #         idle 'gui/sagi/roundbutton-idle.png'
        #         hover 'gui/sagi/roundbutton-hover.png'
        #         action [
        #             Hide('flower_menu_button'),
        #             Show('journal'),
        #         ]
        #     text "j":
        #         align (0.5, 0.5)
        #         text_align 0.5

        # frame at flower_menu_transform:
        #     background None
        #     align (1.0, 0.0)
        #     offset (-110, 100)
        #     imagebutton at flower_button_transform:
        #         align (0.5, 0.5)
        #         idle 'gui/sagi/roundbutton-idle.png'
        #         hover 'gui/sagi/roundbutton-hover.png'
        #         hovered [
        #             HoverFlowerButton(),
        #             Hide('flower_menu_button'),
        #             Show('flower_menu'),
        #             Show('flower_menu_moon'),
        #         ]
        #         action [
        #             TapFlowerButton(),
        #             Hide('flower_menu_button'),
        #             Show('flower_menu'),
        #             Show('flower_menu_moon'),
        #         ]
        #     text "i":
        #         align (0.5, 0.5)
        #         text_align 0.5

        key "K_ESCAPE" action [
            CenterFlower(),
            Hide('flower_menu_button'),
            Show('flower_menu'),
            Show('flower_menu_moon'),
        ]

        key "mouseup_3" action [
            RightClickFlower(),
            Hide('flower_menu_button'),
            Show('flower_menu'),
            Show('flower_menu_moon'),
        ]

init python:
    import math

    _game_menu_screen = None
    right_click_pos = (0, 0)
    tap_mode = False

    flower_menu_actions = [
        ('save', ShowMenu('save')),
        ('load', ShowMenu('load')),
        ('pref', ShowMenu('custom_preferences')),
        ('quit', Quit(confirm=not main_menu)),
        ('menu', MainMenu()),

    ]

    def polygon_point_offset(ind, distance=75, points=5):
        if points == 1:
            ind += 0.5
        elif points > 1:
            ind += (points - 1) * 0.5
        ang = -2.0 * math.pi / points
        x = math.sin(ang * ind) * distance
        y = math.cos(ang * ind) * distance
        return (x, y)

    class HoverFlowerButton:
        def __call__(self):
            global right_click_pos, tap_mode
            dim = (115, 110)
            right_click_pos = (config.screen_width - dim[0], dim[1])
            tap_mode = False

    class TapFlowerButton:
        def __call__(self):
            global right_click_pos, tap_mode
            dim = (115, 110)
            right_click_pos = (config.screen_width - dim[0], dim[1])
            tap_mode = True

    class RightClickFlower:
        def __call__(self):
            global right_click_pos, tap_mode
            dim = (115, 110)
            right_click_pos = list(renpy.get_mouse_pos())
            if config.screen_width - right_click_pos[0] < dim[0]:
                right_click_pos[0] = config.screen_width - dim[0]
            elif right_click_pos[0] < dim[0]:
                right_click_pos[0] = dim[0]
            if right_click_pos[1] < dim[1]:
                right_click_pos[1] = dim[1]
            elif config.screen_height - right_click_pos[1] < dim[1]:
                right_click_pos[1] = config.screen_height - dim[1]
            right_click_pos = tuple(right_click_pos)
            tap_mode = False

    class CenterFlower:
        def __call__(self):
            global right_click_pos, tap_mode
            right_click_pos = (0.5, 0.5)
            tap_mode = False

transform flower_moon_transform:
    anchor (0.5, 0.5)
    on show:
        parallel:
            rotate 0
            linear 5.0 rotate 180
            repeat
        parallel:
            zoom 0.0
            easein 0.2 zoom 1.02
            ease 0.3 zoom 1.0
    on hide:
        easein 0.2 zoom 0.0

screen flower_menu_moon():
    if quick_menu:
        frame at flower_moon_transform:
            background None
            padding (0, 0)
            margin (0, 0)
            pos right_click_pos

            add im.FactorScale('gui/sagi/roundbutton-hover.png', 0.15):
                align (0.5, 0.5)
                xoffset -25
            add im.FactorScale('gui/sagi/roundbutton-hover.png', 0.15):
                align (0.5, 0.5)
                xoffset 25
screen flower_menu():
    if quick_menu:
        button:
            background None
            padding (0, 0)
            margin (0, 0)
            xysize (1.0, 1.0)
            key "mouseup_3" action [
                Hide('flower_menu'),
                Show('flower_menu_button'),
                Hide('flower_menu_moon'),
            ]
            action [
                Hide('flower_menu'),
                Show('flower_menu_button'),
                Hide('flower_menu_moon'),
            ]

        button at flower_menu_transform:
            key_events True
            background None
            padding (0, 0)
            margin (0, 0)
            xysize (800, 800)
            pos right_click_pos

            add im.FactorScale('gui/sagi/roundbutton-hover.png', 0.4):
                align (0.5, 0.5)
            for i in range(0, len(flower_menu_actions)):
                frame:
                    background None
                    padding (0, 0)
                    margin (0, 0)
                    offset polygon_point_offset(i, points=len(flower_menu_actions))
                    imagebutton:
                        align (0.5, 0.5)
                        idle 'gui/sagi/roundbutton-idle.png'
                        hover 'gui/sagi/roundbutton-hover.png'
                        action [
                            Hide('flower_menu'),
                            Show('flower_menu_button'),
                            Hide('flower_menu_moon'),
                            flower_menu_actions[i][1],
                        ]
                        alt flower_menu_actions[i][0]
                    text flower_menu_actions[i][0]:
                        align (0.5, 0.5)
                        yoffset 13
                        text_align 0.5
                        size 15
            action []
            if not tap_mode:
                mousearea:
                    unhovered [
                        Hide('flower_menu'),
                        Show('flower_menu_button'),
                        Hide('flower_menu_moon'),
                    ]
        key "K_ESCAPE" action [
                Hide('flower_menu'),
                Show('flower_menu_button'),
                Hide('flower_menu_moon'),
        ]

transform fade_transform:
    on show:
        alpha 0
        linear 0.3 alpha 1
    on hide:
        linear 0.3 alpha 0

transform journal_transform:
    on show:
        xpos 1.5
        alpha 0
        easein 0.3 xalign 0.4 alpha 1
        easeout 0.1 xalign 0.5
    on hide:
        ease 0.1 xalign 0.4
        easeout 0.3 xpos 1.5 alpha 0

init python:
    import math

    journal_selected_entry = 0

    class JournalSelected:
        def __init__(self, _entry):
            self.entry = _entry

        def __call__(self):
            global journal_selected_entry
            journal_selected_entry = self.entry
            renpy.restart_interaction()

screen journal():
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    style_prefix "journal"

    button at fade_transform:
        background "#000000CC"
        xysize (1.0, 1.0)
        action [
            Hide('journal'),
            Show('flower_menu_button'),
        ]

    frame at journal_transform:
        align (0.5, 0.5)
        xysize (1200, 800)
        margin (0, 0)
        button:
            background None
            xysize (1.0, 1.0)
            action NullAction()
        frame:
            background colors.namebox['Default']
            xysize (255, 55)
            align (0, 0)
            offset (50, -105)
            label "Log":
                xysize (255, 55)
                align (0.5, 0.5)
                text_xalign 0.5
                text_color colors.base

        # frame:
        #     background None
        #     padding (0, 0)
        #     margin (0, 0)
        #     xysize (300, 700)
        #     align (0.0, 0.5)
        #     # LEFT
        #     vbox:
        #         xalign 0.5
        #         xsize 300
        #         button:
        #             style_prefix 'list'
        #             align (0.5, 0.5)
        #             selected journal_selected_entry == 0
        #             text 'Chat log':
        #                 style_prefix 'list_button'
        #             action JournalSelected(0)
        #
        #         text '.    .    .':
        #             xysize (300, 700)
        #             align (0.5, 0.5)
        #         # null height 15
        #         # button:
        #         #     style_prefix 'list'
        #         #     align (0.5, 0.5)
        #         #     selected journal_selected_entry == 1
        #         #     text 'Day 26':
        #         #         style_prefix 'list_button'
        #         #     action JournalSelected(1)
        # # DIVIDER
        frame:
            background colors.neutral
            padding (0, 0)
            margin (0, 0)
            xysize (3, 700)
            align (0.01, 0.5)

        frame:
            background None
            padding (0, 0)
            margin (0, 0)
            xysize (890, 700)
            align (1.0, 0.5)
            xoffset 5
            # RIGHT

            if journal_selected_entry == 0:
                if _history_list:
                    viewport id "history_list":
                        draggable True mousewheel True
                        vbox:
                            xsize 890
                            spacing 15
                            for h in _history_list:
                                if h.who:
                                    hbox:
                                        spacing 10
                                        xsize 890
                                        if h.who:
                                            label h.who:
                                                substitute False
                                                ## Take the color of the who text from the Character, if
                                                ## set.
                                                text_color colors.base
                                                if h.who in colors.namebox:
                                                    background colors.namebox[h.who]
                                                text_size 26
                                                text_align (0.5, 0.5)
                                                xysize (100, 35)
                                        else:
                                            label '':
                                                xysize (100, 35)
                                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                                        label what:
                                            substitute False
                                            xsize 700
                                            text_align (0.0, 0.0)
                                            text_size 30
                                            if "color" in h.what_args:
                                                text_color h.what_args["color"]
                                else:
                                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                                    label what:
                                        substitute False
                                        xsize 850
                                        text_xalign 0.0
                                        text_size 30
                    vbar value YScrollValue("history_list"):
                        xalign -0.063
                else:
                    label _("The chat log is empty."):
                        text_size 32
            else:
                pass

        button:
            xysize (70, 70)
            align (1.0, 0.0)
            offset (52, -85)
            idle_background 'gui/sagi/roundbutton-idle.png'
            hover_background 'gui/sagi/roundbutton-hover.png'
            action [
                Hide('journal'),
                Show('flower_menu_button'),
            ]
            text 'X':
                align (0.5, 0.5)

    ## Right-click and escape answer "no".
    key "game_menu" action [
        Hide('journal'),
        Show('flower_menu_button'),
    ]

style list_button:
    properties gui.button_properties("button")
    idle_background None
    insensitive_background None
    hover_background Frame('gui/sagi/smallbutton-idle.png', Borders(55, 0, 55, 0))
    selected_background Frame('gui/sagi/smallbutton-selected.png', Borders(55, 0, 55, 0))
    xysize (270, 57)

style list_button_text is gui_text:
    properties gui.text_properties("button")
    align (0.5, 0.5)

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.75
            yalign .95
            textbutton _("<") action Rollback() alt "Rollback"
            textbutton _(">") action Preference("auto-forward", "toggle")
            textbutton _(">>") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("LOG") action [
                Hide('flower_menu_button'),
                Show('journal'),
            ]

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
# init python:
#     config.overlay_screens.append("quick_menu")
#     config.overlay_screens.append("flower_menu_button")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xalign
        yalign 0.5

        spacing gui.navigation_spacing

        # if main_menu:
        #     textbutton _("Start") action Start("start")
        # else:
        #     textbutton _("History") action ShowMenu("history")
        #
        #     textbutton _("Save") action ShowMenu("save")
        textbutton _("Start") action Start("start")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("custom_preferences")

        textbutton _("About") action ShowMenu("about")

        if persistent.ending == "Complete":
            textbutton _ ("Gallery") action ShowMenu("gallery")

            textbutton _("Jukebox") action ShowMenu("Jukebox")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        # elif not main_menu:
        #
        #     textbutton _("Main Menu") action MainMenu()

        # textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):

            # ## Help isn't necessary or relevant to mobile devices.
            # textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    idle_color "#000"
    hover_color colors.selected
    outlines [ (3, colors.base, 0, 0) ]

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

init python:
    time = 0.0
    speed = 3.0

    def UpdateRotation(trans, st, at):
        global time, speed
        time += 0.03 * speed
        trans.rotate = time

transform main_menu_bg_transform:
    subpixel True
    anchor (0.5, 0.5)
    zoom 2.2
    align (0.45, 0.45)
    function UpdateRotation
    pause 0.03
    repeat

transform main_menu_bg_restore_transform:
    subpixel True
    anchor (0.5, 0.5)
    zoom 2.2
    align (0.45, 0.45)
    rotate time
    parallel:
        ease 3 rotate 0.0 align (0.5, 0.5)
    parallel:
        pause 1.0
        ease 2.0 zoom 1.5

screen extras():
    tag menu

    #use game_menu(_("")):
    style_prefix "extras"

    add "backgrounds/space.png" at main_menu_bg_transform

    textbutton _("Return"):
        # style "return_button"

        action Return()

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    #add gui.main_menu_background at fade_transform
    add "backgrounds/space.png" at main_menu_bg_transform

    # # This empty frame darkens the main menu.
    # frame:
    #     pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background None

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude
            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 45

    #background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 130
    right_margin 130
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xalign
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_(""), scroll="viewport"):

        style_prefix "about"
        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("{i}A Field of Flowers and Stars{/i} was developed for Yurijam 2019 by Watercress in collaboration with Somnova Studios and Sarchalen Visual Media.\n")

            #text _("If you loved this game, check out our {a=https://watercressstudios.com/}official website{/a}, {a=http://somnovastudios.org/}Somnova Studios{/a}, and {a=https://sarchalen.itch.io/}Sarchalen Visual Media{/a} or go straight to our {a=https://watercress.itch.io/}itch.io page{/a} for more of our projects.\n")

            #text _("Also, we have a {a=https://store.steampowered.com/developer/Watercress/}Steam page{/a} where you can download and play several of our previously published visual novels.\n")

            text _("You can follow the team members on twitter to keep up to date with new studio releases and experience their artwork and other talents.\n")

            text _("{a=https://twitter.com/Wolf_GameDev}Tristan 'Wolf' Barber{/a} (Director, Story Concept, Story Writer, Editor, Sound Editor)\n")

            text _("{a=https://m.imdb.com/name/nm7026286/}Kevin Bomer{/a} (Director, Story Concept,  Story Writer, Scripting)\n")

            text _("{a=https://twitter.com/Hamadyne}Hamadyne{/a} (Story Concept, Story Writer)\n")

            text _ ("{a=https://twitter.com/Hoakkun}A.D. 'Hoa' Hemingway{/a} (Story Writer, Scripting)\n")

            text _ ("Monochrome (Story Concept, Story Writer)\n")

            text _ ("{a=https://twitter.com/Zodai_Stryde}Zodai{/a} (Story Writer, Story Concept, Editor, Scripting)\n")

            text _ ("{a=https://twitter.com/alchworks}TheAlchemyst{/a} (Editing Director, Cinematics Directing, Marketing Director, Logo Design)\n")

            text _ ("{a=https://twitter.com/Paul__Robins}Paul Robins{/a} (Music Director, Sound Design, Sound Editor, Audio)\n")

            text _ ("{a=https://twitter.com/KartProwler}Kart Prowler{/a} (Sprite, CG, Concept Art)\n")

            text _ ("{a=https://twitter.com/Drazillion}Alison 'Draz' Huang{/a} (BG Art)\n")

            text _ ("{a=https://twitter.com/delete_wei}Wei Yuan Lee{/a} (Editor, Scripting)\n")

            text _ ("{a=https://kp1n.bandcamp.com/}Kierious{/a} (Music)\n")

            text _ ( "{a=https://speedyspcfan.bandcamp.com/releases}Noah 'Speedy' Aman{/a} (Music)\n")

            text _ ("{a=https://twitter.com/JaeJaeAgogo}Jae{/a} (Music)\n")

            text _ ("{a=https://twitter.com/TheVoiderling}Voiderling{/a} (Concept Art, CG, BG art)\n")

            text _ ("{a=https://twitter.com/liah0227}Liah{/a} (Concept Art)\n")

            text _ ("{a=https://www.deviantart.com/erezu-kun}Erezu{/a} (BG Art)\n")

            text _ ("{a=https://twitter.com/sagittaeri}Sagittaeri{/a} (UI Design, Scripting Tools)\n")

            text _ ("{a=https://twitter.com/Happinessplus__}Happiness+{/a} (Programming Director)\n")

            text _ ("{a=https://twitter.com/DreadLindwyrm}Steve/DreadLindwyrm{/a} (Development Director)\n")

            text _ ("{a=https://www.deviantart.com/ebagigi}Gabriel 'Ebagigi'{/a} (Scripting)\n")

            text _ ("{a=https://twitter.com/Meyvol}Meyvol{/a} (Scripting)\n")

            text _ ("{a=https://twitter.com/SandraMJdev}Sandra 'SandraMJ' Molina{/a} (Voice Direction)\n")

            text _ ("{a=https://twitter.com/Dottovuu}Dottovu{/a} (VA of Leona)\n")

            text _ ("{a=https://twitter.com/nvansistine}Natalie{/a} (VA of Raine)\n")

            text _ ("{a=https://twitter.com/homulily}Lily Lammers{/a} (VA of Juneau)\n")

            text _ ("{a=https://twitter.com/Bodo1215}Bodo{/a} (Marketing)\n")

            text _ ("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            hbox:
                xalign .5
                #add "images/logos/watercresslogo.png"  zoom 0.13 yalign 0.5 xalign .25
                imagebutton idle "images/logos/watercresslogo.png" action OpenURL("https://watercressstudios.com/")
                imagebutton idle "images/logos/somnovalogo.png" action OpenURL("http://somnovastudios.org/")
                imagebutton idle "images/logos/sarchalenlogo.png" action OpenURL("http://sarchalen.com/")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
#style about_hyperlink_text is hyperlink_text
style about_button_text is gui_button_text
style about_text:
      size 30
      color "#fff"

style about_label_text:
    size gui.label_text_size
    color "#7ECBDD"
style hyperlink_text:
    color "#7ECBDD"
    hover_underline "#7ECBDD"



## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use custom_file_slots(_("Save"))


screen load():

    tag menu

    use custom_file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

screen custom_file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    style_prefix "journal"

    if main_menu:
        add "backgrounds/space.png" at main_menu_bg_transform

    if main_menu:
        $ close_action = [
            Hide('custom_file_slots'),
            Return(),
        ]
    else:
        $ close_action = [
            Hide('custom_file_slots'),
            Show('flower_menu_button'),
            Return(),
        ]
    button at fade_transform:
        background "#000000CC"
        xysize (1.0, 1.0)
        action close_action
    frame at fade_transform:
        align (0.5, 0.5)
        xysize (1200, 800)
        margin (0, 0)
        button:
            background None
            xysize (1.0, 1.0)
            action NullAction()
        frame:
            background colors.namebox['Default']
            xysize (255, 55)
            align (0, 0)
            offset (50, -105)
            label title:
                xysize (255, 55)
                align (0.5, 0.5)
                text_xalign 0.5
                text_color colors.base

        frame:
            background None
            padding (0, 0)
            margin (0, 0)
            xysize (900, 700)
            align (0.5, 0.5)

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                            yoffset 15
                        text FileSaveName(slot):
                            style "slot_name_text"
                            yoffset 15
                        key "save_delete" action FileDelete(slot)

        button:
            xysize (70, 70)
            align (1.0, 0.0)
            offset (52, -85)
            idle_background 'gui/sagi/roundbutton-idle.png'
            hover_background 'gui/sagi/roundbutton-hover.png'
            action close_action
            text 'X':
                align (0.5, 0.5)

    ## Right-click and escape answer "no".
    key "game_menu" action close_action


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

screen custom_preferences():
    tag menu

    if main_menu:
        $ close_action = [
            Hide('custom_preferences'),
            Return(),
        ]
    else:
        $ close_action = [
            Hide('custom_preferences'),
            Show('flower_menu_button'),
            Return(),
        ]
    if main_menu:
        add "backgrounds/space.png" at main_menu_bg_transform
    button at fade_transform:
        background "#000000CC"
        xysize (1.0, 1.0)
        action close_action
    frame at fade_transform:
        align (0.5, 0.5)
        xysize (1200, 600)
        margin (0, 0)
        button:
            background None
            xysize (1.0, 1.0)
            action NullAction()
        frame:
            background colors.namebox['Default']
            xysize (330, 55)
            align (0, 0)
            offset (50, -105)
            label "Preferences":
                xysize (255, 55)
                align (0.5, 0.5)
                text_xalign 0.5
                text_color colors.base

        frame:
            background None
            padding (0, 0)
            margin (0, 0)
            xysize (900, 550)
            align (0.5, 0.5)
            offset (-10, -30)

            vbox:
                spacing 10
                xysize (900, 550)
                align (0.5, 0.5)
                null height 0
                frame:
                    background None
                    padding (0, 0)
                    margin (0, 0)
                    xysize (780, 200)
                    align (0.5, 0.5)
                    hbox:
                        spacing 10
                        if renpy.variant("pc"):
                            vbox:
                                xsize 230
                                style_prefix "radio"
                                label _("Display"):
                                    text_size 32
                                null height 10
                                textbutton _("Window") action Preference("display", "window"):
                                    xsize 250
                                    text_xalign 0.0
                                    text_xpos 12
                                    text_yoffset -15
                                    yoffset 1
                                textbutton _("Fullscreen") action Preference("display", "fullscreen"):
                                    xsize 250
                                    text_xalign 0.0
                                    text_xpos 12
                                    text_yoffset -15
                        vbox:
                            xsize 260
                            style_prefix "check"
                            label _("Skip"):
                                text_size 32
                            null height 10
                            textbutton _("Unseen Text") action Preference("skip", "toggle"):
                                xsize 250
                                text_xalign 0.0
                                text_yoffset -15
                                text_xpos 12
                            # textbutton _("After Choices") action Preference("after choices", "toggle"):
                            #     xsize 250
                            #     text_xalign 0.0
                            #     text_xpos 12
                            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")):
                                xsize 250
                                text_xalign 0.0
                                text_yoffset -15
                                text_xpos 12

                        ## Additional vboxes of type "radio_pref" or "check_pref" can be
                        ## added here, to add additional creator-defined preferences.

                        hbox:
                            xsize 260
                            style_prefix "slider"
                            box_wrap True
                            vbox:
                                label _("Text Speed"):
                                    text_size 32
                                bar value Preference("text speed"):
                                    xsize 280
                                label _("Auto-Forward Time"):
                                    text_size 32
                                bar value Preference("auto-forward time"):
                                    xsize 280
                frame:
                    background None
                    padding (0, 0)
                    margin (0, 0)
                    xysize (800, 250)
                    align (0.5, 0.5)
                    vbox:
                        if config.has_music:
                            label _("Music Volume"):
                                text_size 32
                            hbox:
                                bar value Preference("music volume")
                        if config.has_sound:
                            label _("Sound Volume"):
                                text_size 32
                            hbox:
                                bar value Preference("sound volume")
                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)
                        if config.has_voice:
                            label _("Voice Volume"):
                                text_size 32
                            hbox:
                                bar value Preference("voice volume")
                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice)
                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing
                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                text_yoffset -15
                                style "mute_all_button"

        button:
            xysize (70, 70)
            align (1.0, 0.0)
            offset (52, -85)
            idle_background 'gui/sagi/roundbutton-idle.png'
            hover_background 'gui/sagi/roundbutton-hover.png'
            action close_action
            text 'X':
                align (0.5, 0.5)

    key "K_ESCAPE" action close_action

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 350

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 600


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    if main_menu:
        add "backgrounds/space.png" at main_menu_bg_transform
    add "#000000CC" at fade_transform

    frame at fade_transform:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/sagi/frame.png", gui.confirm_frame_borders)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

# style confirm_button:
#     properties gui.button_properties("confirm_button")
#
# style confirm_button_text:
#     properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900


transform announce_inout:
    on show:
        alpha 0
        linear 1.5 alpha 1
    on hide:
        linear 1.5 alpha 0

screen tobecontinued_announce():
    frame align (0.5, 0.4) at announce_inout:
        background None
        padding (100,100,100,100)
        text 'The End':
            align (0.5, 0.5)
            text_align 0.5
            size 100
            color '#fff'
    timer 2 action Return()

init python:
    demo_letter_text = """Thanks for playing our demo, everyone!

We hope you enjoyed this short introduction to our game! The full game will be updated and revised, and the game itself will be around 15,000 words long. In the meantime, come hang out with us on Discord to meet the devs and to check out our other fun projects!

We will see you in itch.io and Steam when the time comes!

~A Field of Flowers and Stars Development Team

https://discord.gg/watercress"""

screen demo_letter():
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    style_prefix "journal"

    button at fade_transform:
        background "#000000CC"
        xysize (1.0, 1.0)
        action Return()

    frame at fade_transform:
        align (0.5, 0.5)
        xysize (1200, 800)
        margin (0, 0)
        button:
            background None
            xysize (1.0, 1.0)
            action NullAction()

        frame:
            background None
            padding (0, 0)
            margin (0, 0)
            xysize (850, 750)
            align (0.5, 0.5)
            text demo_letter_text:
                size 32
                align (0.5, 0.5)

        button:
            xysize (70, 70)
            align (1.0, 0.0)
            offset (52, -85)
            idle_background 'gui/sagi/roundbutton-idle.png'
            hover_background 'gui/sagi/roundbutton-hover.png'
            action Return()
            text 'X':
                align (0.5, 0.5)

    ## Right-click and escape answer "no".
    key "game_menu" action Return()

#
# Generate credits screen based on parameters below
#

init python:
    credits_duration = 30.0
    credits_height = 3550
    credits_content = [
        ( "Developed for Yurijam 2019.",
            [
            ]
        ),
        ( "Directing",
            [
                "Tristan 'Wolf' Barber",
                "Kevin Bomer",
            ]
        ),
        ( "Story",
            [
                (
                    "Writing",
                    "Tristan 'Wolf' Barber",
                    "Kevin Bomer",
                    "Hamadyne",
                    "A.D. 'Hoa' Hemingway",
                    "Monochrome",
                ),
                (
                    "Story Concept",
                    "Zodai",
                ),
            ]
        ),
        ( "Editing Directing",
            [
                "TheAlchemyst",
            ]
        ),
        ( "Editing",
            [
                "Tristan 'Wolf' Barber",
                "Wei Yuan Lee",
                "Zodai",
            ]
        ),
        ( "Audio",
            [
                (
                    "Music Directing",
                    "Paul Robins",
                ),
                (
                    "Music",
                    "Kierious",
                    "Noah 'Speedy' Aman",
                    "Jae",
                ),
                (
                    "Sound Design",
                    "Paul Robins",
                ),
                (
                    "Sound Editing",
                    "Paul Robins",
                    "Tristan 'Wolf' Barber",
                ),
            ]
        ),

        ( "Art",
            [
                (
                    "Sprite",
                    "Kart Prowler",
                ),
                (
                    "Concept Art",
                    "Voiderling",
                    "Liah",
                    "Kart Prowler",
                ),
                (
                    "CG Art",
                    "Kart Prowler",
                ),
                (
                    "BG Art",
                    "Erezu",
                    "Alison 'Draz' Huang",
                    "Voiderling",
                ),
                (
                    "UI Design and Art",
                    "Sagittaeri",
                ),
                (
                    "Logo Design",
                    "TheAlchemyst",
                ),
            ]
        ),

        ( "Code",
            [   (
                    "Director of Programming Department",
                    "Happiness+",
                ),
                (
                    "Development Director",
                    "Steve/DreadLindwyrm",
                ),
                (
                    "Tools and UI",
                    "Sagittaeri",
                ),
            ]
        ),

        ( "Ren'py Scripting",
            [
                (
                    "General",
                    "Kevin Bomer",
                    "Gabriel (Ebagigi)",
                    "Sagittaeri",
                    "Wei Yuan Lee",
                    "A.D. 'Hoa' Hemingway",
                    "Zodai",
                    "Meyvol",
                ),
                (
                    "Audio",
                    "Paul Robins",
                ),
            ]
        ),

        ( "Voice Direction",
            [
                "Sandra 'SandraMJ' Molina",
            ]
        ),
        ( "Voice Overs",
            [
                (
                    "Leona",
                    "Dottovu",
                ),
                (
                    "Raine",
                    "Natalie",
                ),
                (
                    "Juneau",
                    "Lily Lammers",
                ),
            ]
        ),

        ( "Marketing Directing",
            [
                "TheAlchemyst",
            ]
        ),
        ( "Marketing",
            [
                "Bodo",
            ]
        ),
        ( "Cinematics Directing",
            [
                "TheAlchemyst",
            ]
        ),

        ( "Special thanks to",
            [
                "Ren'py Tom",
                "The Lemmasoft Forum",
                "Our Fans",
            ]
        ),
        ( "A thank you to all of our Patrons, including",
            [
                "Merritt Barber",
                "Jonas Lee",
                "TheAlchemyst",
            ]
        ),
    ]

transform credits_roll(duration, dest):
    on show:
        alpha 0 pos (0, 0)
        parallel:
            linear duration ypos -dest
        parallel:
            linear 1 alpha 1
    on hide:
        linear 1 alpha 0

screen credits():
    if not main_menu:
        timer (credits_duration-2) action Return()
        key "dismiss" action Return()
    else:
        timer (credits_duration-2) action Hide("credits")
        key "dismiss" action Hide("credits")
    frame at credits_roll(credits_duration, credits_height):
        background "#000"
        xsize 1920
        vbox:
            xalign 0.5
            null height 500
            for title, names in credits_content:
                null height 50
                text title:
                    text_align 0.5
                    xalign 0.5
                    size 50
                    color "#7ECBDD"
                for name in names:
                    if type(name) == type(()):
                        hbox:
                            xalign 0.5
                            frame:
                                background None
                                padding (0,0,0,0)
                                margin (0,0,0,0)
                                xsize 900
                                text name[0]:
                                    text_align 1.0
                                    xalign 1.0
                                    size 30
                                    color "#fff"
                            null width 50
                            frame:
                                background None
                                padding (0,0,0,0)
                                margin (0,0,0,0)
                                xsize 900
                                vbox:
                                    for n in name[1:]:
                                        text n:
                                            text_align 0.0
                                            xalign 0.0
                                            size 30
                                            color "#fff"
                    else:
                        text name:
                            text_align 0.5
                            xalign 0.5
                            size 30
                            color "#fff"
            null height 5000
