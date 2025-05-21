import pygame
import random
import os

number = random.randint(1,7)

def afficher_interface_combat(screen):
    # Chargement de l'image de fond
    background_path = os.path.join("assets/img", "arène", f"arène{number}.png")
    background_img = pygame.image.load(background_path).convert()
    background_img = pygame.transform.scale(background_img, (1075, 717))
    # Affiche l'image de fond
    screen.blit(background_img, (0, 0))

   
