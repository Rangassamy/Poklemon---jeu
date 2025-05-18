import pygame
from scenes.menu_scene import draw_menu
from scenes.poklemon_scene import draw_poklemon
from scenes.combat_scene import draw_combat
from logic.combat_logic import combat, Poklemon, p1, p2


pygame.init()
screen = pygame.display.set_mode((800, 600))
current_scene = "menu"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                current_scene = "poklemon"
            elif event.key == pygame.K_m:
                current_scene ="menu"
            elif event.key == pygame.K_c:
                current_scene ="combat"
                # Lancer le combat
                combat(Poklemon(**p1), Poklemon(**p2))
    if current_scene == "menu":
        draw_menu(screen)
    elif current_scene == "poklemon":
        draw_poklemon(screen)
    elif current_scene == "combat":
        draw_combat(screen)
        

    pygame.display.flip()
   


pygame.quit()


