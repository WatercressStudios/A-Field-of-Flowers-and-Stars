init python:
    musicbox_content = [
        ( "Music/A Future Together.ogg", "A Future Together", "Paul Robins"),
        ( "Music/Aster.ogg", "Aster", "Paul Robins"),
        ( "Music/Consequence.ogg", "Consequence", "Jae"),
        ( "Music/Critical .ogg", "Critical", "Speedy"),
        ( "Music/Fading Glow.ogg","Fading Glow", "Kieren 'Kierious' Eller"),
        ( "Music/First Night.ogg", "First Night", "Paul Robins"),
        ( "Music/Friends and Family.ogg", "Friends and Family", "Paul Robins"),
        ( "Music/Juneau.ogg", "Juneau", "Jae"),
        ( "Music/main menu.ogg", "Main Menu", "Speedy"),
        ( "Music/meeting leona.ogg", "Meeting Leona", "Speedy"),
        ( "Music/Missing Juneau.ogg", "Missing Juneau", "Speedy"),
        ( "Music/Raine Gets Lost.ogg", "Raine Gets Lost", "Paul Robins"),
        ( "Music/Smugglers and Bombs.ogg", "Smugglers and Bombs", "Speedy"),
        ( "Music/There's No Time.ogg", "There's No Time", "Jae"),
        ( "Music/Trust In You.ogg", "Trust In You", "Paul Robins"),
        ( "Music/wormhole.ogg", "Entering Wormhole", "Speedy"),
    ]

    musicbox_currently_playing = None
screen Jukebox():
    tag menu

    if main_menu:
        add "backgrounds/space.png" at main_menu_bg_transform

    $ close_action = [
        Return(),
    ]
    button at fade_transform:
        background None
        xysize (1.0, 1.0)
        action close_action
    frame at fade_transform:
        align (0.5, 0.5)
        xysize (850, 900)
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
            label "Jukebox":
                xysize (255, 55)
                align (0.5, 0.5)
                text_xalign 0.5
                text_color colors.base

        frame:
            background None
            padding (0, 0)
            margin (0, 0)
            xysize (650, 800)
            align (0.5, 0.5)

            vpgrid xoffset -10:
                cols 1
                mousewheel True
                draggable True
                scrollbars "vertical"
                side_xalign 0.5
                yinitial 0.0
                yspacing 20

                for i in range(len(musicbox_content)):
                    $ clip, title, artist = musicbox_content[i]
                    frame:
                        background None
                        xsize 500
                        ysize 100
                        padding (0,0,0,0)
                        right_margin 20
                        xalign 0
                        imagebutton:
                            idle Frame("gui/sagi/smallbutton-idle.png", Borders(30,30,30,30))
                            hover Frame("gui/sagi/smallbutton-highlighted.png", Borders(30,30,30,30))
                            if i == musicbox_currently_playing:
                                action [ SetVariable("musicbox_currently_playing", None), Play("music", "music/main menu.ogg") ]
                            else:
                                action [ SetVariable("musicbox_currently_playing", i), Play("music", clip) ]
                        frame:
                            background None
                            xsize 500
                            ysize 100
                            padding (30,15,30,15)
                            right_margin 20
                            xalign 0

                            text title pos (0, -5):
                                size 36
                                outlines []
                            text "by " + artist pos (0, 40):
                                size 28
                                outlines []
                            fixed pos (375,5):
                                if i == musicbox_currently_playing:
                                    add "gui/sagi/gui-musicbox-pause.png"
                                else:
                                    add "gui/sagi/gui-musicbox-play.png"

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
