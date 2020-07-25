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
        add "bg black"
    fixed align(0.5,0.5):
        xfit True
        yfit True
        add item
    key "dismiss" action Hide("gallery_item")


screen gallery():
    frame at fade_transform:
        background "images/backgrounds/space.png"
        xsize 1920
        ysize 1200
        align (0.10, 0.10)
        padding (0,0,0,0)
        frame:
            pos (50, 210)
            background None
            padding (0,0,0,0)
            xsize 1850
            ysize 1000
            vpgrid:
                cols 4
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
                            background At("bg black", gallery_thumbnail)
                            xsize 184
                            ysize 116
                            padding (0,0,0,0)
                            fixed align(0.5,0.5):
                                xfit True
                                yfit True
                                add At(pic, gallery_thumbnail)
                            label title pos (0, 10)
                            label "by " + artist pos (0, 150)
                            button action Show("gallery_item", item=pic)
        fixed pos (1565,918):
            imagebutton offset (-40, -5):
                idle "gui/sagi/button-idle.png"
                hover "gui/sagi/button-highlighted.png"
                #if in_main_menu:
                  #  action [ Play("sound", uisound()), Hide("custom_title_extras"), Show("custom_title_center2right") ]
                #else:
                   # action [ Play("sound", uisound()), Return() ]
            # text "Back":
            #     font "BebasNeue-Regular.otf"
            #     size 60
            #     color "#36428A"
            #     outlines []