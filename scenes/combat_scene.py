import pygame
import random
import os
import requests
import io

image_cache = {}

def charger_image_depuis_url(url):
    if url in image_cache:
        return image_cache[url]

    try:
        response = requests.get(url)
        image = pygame.image.load(io.BytesIO(response.content)).convert_alpha()
        image_cache[url] = image  # cache l’image
        return image
    except:
        return None


number = random.randint(1,6)


def afficher_interface_combat(screen, p1, p2, log_combat):
    # Affiche le fond de combat
    background_path = os.path.join("assets/img", "arène", f"arène{number}.png")
    background_img = pygame.image.load(background_path).convert()
    background_img = pygame.transform.scale(background_img, (1075, 717))
    screen.blit(background_img, (0, 0))



    font = pygame.font.SysFont("Arial", 20)

    imagep1 = pygame.transform.scale(charger_image_depuis_url(p1.image), (350, 350))
    imagep1 = pygame.transform.flip(imagep1, True, False)
    screen.blit(imagep1, (100, 300))
    imagep2 = pygame.transform.scale(charger_image_depuis_url(p2.image), (350, 350))
    screen.blit(imagep2, (600, 300))

    bouton_attaque = pygame.Rect(50, 50, 200, 50)
    bouton_defense = pygame.Rect(300, 50, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), bouton_attaque)
    pygame.draw.rect(screen, (0, 0, 255), bouton_defense)


    font = pygame.font.SysFont("Arial", 24)
    txt_att = font.render("ATTAQUER", True, (255, 255, 255))
    txt_def = font.render("DÉFENDRE", True, (255, 255, 255))
    screen.blit(txt_att, (bouton_attaque.x + 20, bouton_attaque.y + 10))
    screen.blit(txt_def, (bouton_defense.x + 20, bouton_defense.y + 10))

    affichage_log = pygame.Rect(600, 50, 450, 200)
    pygame.draw.rect(screen, (125, 125, 125), affichage_log)

    for i, ligne in enumerate(log_combat.split("\n")):
        
        texte = font.render(ligne, True, (0, 0, 0))
        screen.blit(texte, (600, 50 + i * 25))  # ligne suivante = +25 px
  
    

    return bouton_attaque, bouton_defense


