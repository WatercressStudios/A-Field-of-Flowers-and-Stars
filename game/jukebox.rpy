# init python:
#     musicbox_content = [
#         ( "Music/Main Menu.ogg", "Menu Theme", "Paul Robins"),
#         ( "Music/RW_Intro.ogg", "Memories of You", "Paul Robins"),
#         ( "Music/Hub.ogg", "HU8 W0RLD", "Kieren 'Kierious' Eller"),
#         ( "Music/Uninstall_Button.ogg", "Uninstall Button", "Speedy"),
#         ( "Music/RW_S1.ogg","The World Keeps Turning", "Paul Robins"),
#         ( "Music/Awoo_Mug.ogg", "You Were so Strong", "Speedy"),
#         ( "Music/Cat.ogg", "Apologies", "Kieren 'Kierious' Eller"),
#         ( "Music/8_Track.ogg", "Our Song", "Raymond Demers"),
#         ( "Music/RW_S2.ogg", "Sustenance", "Paul Robins"),
#         ( "Music/RW_S3.ogg", "Only The Good Die Young", "Paul Robins"),
#         ( "Music/RW_S4.ogg", "Friendships", "Paul Robins"),
#         ( "Music/Plane_Ticket.ogg", "What Could Have Been", "Speedy"),
#     ]

    # musicbox_currently_playing = None
screen Jukebox():
    tag menu

    style_prefix "main_menu"

    #add gui.main_menu_background at fade_transform
    add "backgrounds/space.png" at main_menu_bg_transform



    