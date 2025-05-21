import pygame
import random
import os
from logic.combat_logic import lancement_du_choix






def afficher_interface_choix(screen):
    # Chargement de l'image de fond
    background_path = os.path.join("assets", "img", f"choix_background.png")
    background_img = pygame.image.load(background_path).convert()
    background_img = pygame.transform.scale(background_img, (1075, 717))
    # Affiche l'image de fond
    screen.blit(background_img, (0, 0))
    lancement_du_choix(screen)
   
