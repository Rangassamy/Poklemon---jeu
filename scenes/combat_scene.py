import pygame
import random
import os

number = random.randint(1,6)


def afficher_interface_combat(screen, p1, p2, log_combat):
    # Affiche le fond de combat
    background_path = os.path.join("assets/img", "arène", f"arène{number}.png")
    background_img = pygame.image.load(background_path).convert()
    background_img = pygame.transform.scale(background_img, (1075, 717))
    screen.blit(background_img, (0, 0))


    # Affiche les noms des pokémon
    font = pygame.font.SysFont("Arial", 20)
    nom1 = font.render(p1.nom, True, (0, 0, 0))
    nom2 = font.render(p2.nom, True, (0, 0, 0))
    screen.blit(nom1, (100, 50))
    screen.blit(nom2, (800, 50))


    bouton_attaque = pygame.Rect(100, 600, 200, 50)
    bouton_defense = pygame.Rect(350, 600, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), bouton_attaque)
    pygame.draw.rect(screen, (0, 0, 255), bouton_defense)


    font = pygame.font.SysFont("Arial", 24)
    txt_att = font.render("ATTAQUER", True, (255, 255, 255))
    txt_def = font.render("DÉFENDRE", True, (255, 255, 255))
    screen.blit(txt_att, (bouton_attaque.x + 20, bouton_attaque.y + 10))
    screen.blit(txt_def, (bouton_defense.x + 20, bouton_defense.y + 10))
    
    log_txt = font.render(log_combat, True, (0, 0, 0))
    screen.blit(log_txt, (100, 500))


    return bouton_attaque, bouton_defense


