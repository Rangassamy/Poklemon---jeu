import pygame
from scenes.combat_scene import afficher_interface_combat

pygame.init()
screen = pygame.display.set_mode((1075, 717))
pygame.display.set_caption("Poklemon - Démo Combat")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Affiche juste l'interface (pas de combat actif)
    afficher_interface_combat(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

import pygame
