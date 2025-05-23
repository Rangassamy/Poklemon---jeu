from pygame import *



def affichage_home(screen):
    RESOLUTION = (1075, 717)
    fonts = font.Font("Assets/PixelPolice.ttf", 15)

    dark_layer = Surface(RESOLUTION, SRCALPHA)
    draw.rect(dark_layer, (20, 20, 20, 150), (0, 0, *RESOLUTION))

    bg = transform.scale(image.load('Assets/img/menu_bg.png'), RESOLUTION)
    logo = transform.smoothscale(image.load('Assets/img/logo.png'), (250, 167))

    # Textes
    title_fonts = font.Font("Assets/PixelPolice.ttf", 80)
    title_text = title_fonts.render("Poklemon", True, (255, 255, 255))

    subtitle_fonts = font.Font("Assets/PixelPolice.ttf", 35)
    subtitle_note_text = subtitle_fonts.render("note", True, (255, 255, 255))
    subtitle_menu_text = subtitle_fonts.render("menu", True, (255, 255, 255))
    credits_text = fonts.render("by Nolan, Erwan and Enzo", True, (255, 255, 255))

    note_fonts = font.Font("Assets/PixelPolice.ttf", 12)
    notes = [
    "pour une fois, le trio n'a pas essayé de faire mieux",
    "que l'autre. Ils ont uni leurs forces, travaillé en",
    "équipe... et ce qui en est sorti risque bien de vous",
    "surprendre.",
    "bonne session à vous !",
    "© 2025 Poklemon Team"
    ]
    note_renders = [note_fonts.render(line, True, (255, 255, 255)) for line in notes]

    control_text = fonts.render("CENTRE DE CONTROLE", True, (255, 255, 255))
    control_button = control_text.get_rect(center=(180, 460))

# start_text = fonts.render("ARENE DE COMBAT", True, (255, 255, 255))
# start_button = start_text.get_rect(center=(165, 530))

# histoir_text = fonts.render("MODE HISTOIRE", True, (255, 255, 255))
# histoir_button = histoir_text.get_rect(center=(155, 600))
    screen.blit(bg, (0,0))
    screen.blit(dark_layer, (0,0))
    screen.blit(logo, (700, 20))
    screen.blit(title_text, (80, 40))
    screen.blit(credits_text, (80, 130))

    screen.blit(subtitle_menu_text, (80, 330))
    screen.blit(subtitle_note_text, (800, 330))

    for i, text in enumerate(note_renders):
        screen.blit(text, (RESOLUTION[0] - 30 - text.get_width(), 400 + i * 25))

    # screen.blit(start_text, start_button)
    screen.blit(control_text, control_button)
    # screen.blit(histoir_text, histoir_button)

    if control_button.collidepoint(mouse.get_pos()):
        draw.rect(screen, (255, 255, 255), (control_button.left - 10, control_button.bottom + 5,control_button.width + 20, 3))
    # if start_button.collidepoint(mouse.get_pos()):
    #     draw.rect(root, (255, 255, 255), (start_button.left - 10, start_button.bottom + 5, start_button.width + 20, 3))
    # if histoir_button.collidepoint(mouse.get_pos()):
    #     draw.rect(root, (255, 255, 255), (histoir_button.left - 10, histoir_button.bottom + 5, histoir_button.width + 20, 3))

            # if control_button.collidepoint(events.pos):
            #     # StartControl()
            # # if start_button.collidepoint(events.pos):
            # #     StartArene()
            # # if histoir_button.collidepoint(events.pos):
            # #     StartHistoir()
