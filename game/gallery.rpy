#
# Generate gallery screen based on parameters below
#

init python:
    gallery_content = [
        ( "cgtree", "Tree", "Voiderling"),
        ( "kiss1", "The Kiss", "Kart Prowler"),
        ( "kiss2", "Midst of Kiss", "Kart Prowler"),
        ( "kiss3", "Kiss Finally", "Kart Prowler"),
        ( "kiss4", "Eyes Open", "Kart Prowler"),
        ( "asteroidfield", "Asteroid Field", "Voiderling"),
        ( "forest", "Forest", "Erezu"),
        ( "stars", "Stars", "Erezu"),
        ( "cave", "Cave", "Erezu"),
        ( "street", "Aster City", "Erezu"),
    ]

image black = Solid("#000")

transform gallery_thumbnail:
    xzoom 0.2
    yzoom 0.2

screen gallery_item(item):
    fixed at fade_transform:
        add "#000c"
    fixed align(0.5,0.5) at fade_transform:
        xfit True
        yfit True
        add item:
            zoom 0.75
    key "dismiss" action Hide("gallery_item")


screen gallery():
    tag menu
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
        background None
        xysize (1.0, 1.0)
        action close_action
    frame at fade_transform:
        align (0.5, 0.5)
        xysize (1600, 900)
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
            label "Gallery":
                xysize (255, 55)
                align (0.5, 0.5)
                text_xalign 0.5
                text_color colors.base

        frame:
            background None
            padding (0, 0)
            margin (0, 0)
            xysize (1400, 800)
            align (0.5, 0.5)

            vpgrid:
                cols 3
                mousewheel True
                draggable True
                scrollbars "vertical"
                side_xalign 0.50
                yinitial 0.0
                xspacing 0
                yspacing 0

                for pic, title, artist in gallery_content:
                    frame:
                        background None
                        xsize 414
                        ysize 246
                        padding (0,15,20,15)

                        frame:
                            background None
                            xsize 394
                            ysize 216
                            padding (0,0,0,0)
                            fixed align(0.5,0.5):
                                xfit True
                                yfit True
                                add Crop((10, 15, 394, 216),At(pic, gallery_thumbnail))
                            button action Show("gallery_item", item=pic):
                                idle_background "#000a"
                                hover_background None
                                xsize 394
                                ysize 216
                            label title pos (10, 130):
                                xsize 414
                                text_color "000"
                                text_size 30
                                text_outlines [(2, 'fff'), ]
                            label "by " + artist pos (10, 170):
                                xsize 414
                                text_color "000"
                                text_size 24
                                text_outlines [(2, 'fff'), ]

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
