import pygame
from scenes.choix_scene import afficher_interface_choix
from scenes.combat_scene import afficher_interface_combat
from logic.combat_logic import zones_clickables, choix_poklemon, creer_poklemon, tour_de_jeu
import random
from scenes.home_scene import affichage_home
from pygame import *
import time

pygame.init()
screen = pygame.display.set_mode((1075, 717))
pygame.display.set_caption("Poklemon - Démo jeu")

running = True
clock = pygame.time.Clock()

etat = "home"
combat_en_cours = False
log_combat = ""
p1 = None
vainqueur = None
tour = 1
fonts = font.Font("Assets/PixelPolice.ttf", 15)
control_text = fonts.render("CENTRE DE CONTROLE", True, (255, 255, 255))
control_button = control_text.get_rect(center=(180, 460))
bouton_attaque = None
bouton_defense = None


while running:
    if etat == "home":
        affichage_home(screen)
    elif etat == "selection":
        afficher_interface_choix(screen)
    elif etat == "combat":
        bouton_attaque, bouton_defense = afficher_interface_combat(screen, p1, p2, log_combat)
        if p1.vitesse >= p2.vitesse:
            tour_joueur = p1
            tour_bot = p2
        else:
            tour_joueur = p2
            tour_bot = p1
   


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
                        if p1.vitesse > p2.vitesse:
                            rapidos = p1.nom
                        else:
                            rapidos = p2.nom
                        log_combat = "Combat engagé ! c'est au tour de " + rapidos
            if etat == "home":
                if control_button.collidepoint(event.pos):
                  etat = "selection"
                 



            elif etat == "combat" and vainqueur == None:
                if bouton_attaque and bouton_defense and bouton_attaque.collidepoint(event.pos):           
                    if vainqueur is None:  # on ne joue plus si le combat est terminé
                       
                        log_combat = tour_de_jeu(tour_joueur, tour_bot, joueur_est_humain=True, action="attaquer")
                        
                        if tour_bot.is_alive():
                            log_combat += "\n" + tour_de_jeu(tour_bot, tour_joueur, joueur_est_humain=False)

                        tour += 1

                        # après les deux actions, on vérifie s’il y a un vainqueur
                        if not p1.is_alive():
                            vainqueur = p2.nom
                            log_combat += f"\n{p2.nom} a gagné ! fin de la manche {tour}"
                        elif not p2.is_alive():
                            vainqueur = p1.nom
                            log_combat += f"\n{p1.nom} a gagné ! fin de la manche {tour}"

                    
                    
                elif bouton_attaque and bouton_defense and bouton_defense.collidepoint(event.pos):
                    if vainqueur is None:  # on ne joue plus si le combat est terminé
                        log_combat = tour_de_jeu(tour_joueur, tour_bot, joueur_est_humain=True, action="defendre")
                        
                        if tour_bot.is_alive():
                            log_combat += "\n" + tour_de_jeu(tour_bot, tour_joueur, joueur_est_humain=False)

                        tour += 1

                        # après les deux actions, on vérifie s’il y a un vainqueur
                        if not p1.is_alive():
                            vainqueur = p2.nom
                            log_combat += f"\n{p2.nom} a gagné ! fin de la manche {tour}"
                        elif not p2.is_alive():
                            vainqueur = p1.nom
                            log_combat += f"\n{p1.nom} a gagné ! fin de la manche {tour}"    
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

import pygame
