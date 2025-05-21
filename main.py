import pygame
from scenes.choix_scene import afficher_interface_choix
from scenes.combat_scene import afficher_interface_combat
from logic.combat_logic import zones_clickables, choix_poklemon, creer_poklemon, tour_de_jeu
import random

pygame.init()
screen = pygame.display.set_mode((1075, 717))
pygame.display.set_caption("Poklemon - Démo Combat")

running = True
clock = pygame.time.Clock()

etat = "selection"
combat_en_cours = False
log_combat = ""
p1 = None
p2 = None


while running:
    if etat == "selection":
        afficher_interface_choix(screen)
    elif etat == "combat":
        bouton_attaque, bouton_defense = afficher_interface_combat(screen, p1, p2, log_combat)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.MOUSEBUTTONDOWN:
            if etat == "selection":
                for rect, poklemon in zones_clickables:
                    if rect.collidepoint(event.pos): 
                        p1 = poklemon
                        p2 = creer_poklemon(random.choice([x for x in choix_poklemon if x["name"] != p1.nom]))
                        etat = "combat"
                        combat_en_cours = True
                        log_combat = "Combat engagé !"



            elif etat == "combat":
                if bouton_attaque.collidepoint(event.pos):
                    log_combat = "Tu as attaqué !" 
                    
                    
                elif bouton_defense.collidepoint(event.pos):
                    log_combat = "Tu t'es défendu !"    
    

        


    pygame.display.flip()
    clock.tick(30)

pygame.quit()

import pygame
