import time
import random
import json
import os
import pygame
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


class Poklemon:
    def __init__(self, nom, type_, hp, attaque, defense, vitesse, image):
        self.nom = nom
        self.type = type_
        self.hp = hp
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse
        self.en_defense = False  # état actif pour le tour
        self.image = image

    def is_alive(self):
        return self.hp > 0

    def prendre_degats(self, degats):
        if self.en_defense:
            degats = degats // 2
        self.hp -= degats
        if self.hp < 0:
            self.hp = 0

    def __str__(self):
        return f"{self.nom} [{self.type}] HP:{self.hp} ATQ:{self.attaque} DEF:{self.defense} VIT:{self.vitesse} IMG:{self.image}"


# Chemin relatif vers le fichier JSONL
data_path = os.path.join("data", "pokemons_base.jsonl")

def charger_pokemons():
    pokemons = []
    with open(data_path, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())  # ligne = un pokémon
            pokemons.append(data)
    return pokemons

poklemon_array = charger_pokemons()

def creer_poklemon(donnees):
    return Poklemon(
        nom=donnees["name"],
        type_="/".join(donnees["types"]),  # on fusionne les types en une seule chaîne
        hp=donnees["stats"]["hp"],
        attaque=donnees["stats"]["attack"],
        defense=donnees["stats"]["defense"],
        vitesse=donnees["stats"]["speed"],
        image = donnees["image_url"]
    )

def generer_selection_poklemon():
    taille_liste = len(poklemon_array)
    nb_choices = 10
    
    # point de départ aléatoire (en évitant de dépasser la fin)
    start_index = random.randint(0, taille_liste - nb_choices)
    sous_liste = poklemon_array[start_index:start_index + nb_choices]
    array = []
    for poklemon in sous_liste: 
        array.append(poklemon)
    return array

choix_poklemon = generer_selection_poklemon()


zones_clickables = []

def lancement_du_choix(screen):
    zones_clickables.clear()
    font = pygame.font.SysFont("Arial", 20)
    for i, poklemon in enumerate(choix_poklemon):
        colonne = i % 5
        ligne = i // 5
        x = 40 + colonne * (160 + 50)
        y = 60 + ligne * (200 + 20)
        nom_texte = font.render(poklemon["name"], True, (0, 0, 0))
        hp_texte = font.render("HP : " + str(poklemon["stats"]["hp"]), True, (0, 0, 0))
        pok_obj = creer_poklemon(poklemon)
        rect = pygame.Rect( x, y, 160, 200)
        pygame.draw.rect(screen, (115, 115, 115), rect, border_radius=10)
        text_rect = nom_texte.get_rect(center=(x + 160 // 2, y + 200 - 60))
        screen.blit(nom_texte, text_rect)
        text_hp_rect = hp_texte.get_rect(center=(x + 160 // 2, y + 200 - 40))
        screen.blit(hp_texte, text_hp_rect)
        image = charger_image_depuis_url(pok_obj.image)
        if image:
            image = pygame.transform.scale(image, (100, 100))
            screen.blit(image, (x + 40, y + 20))

        zones_clickables.append((rect, pok_obj))


def calcul_degats(attaquant, defenseur):
    base = attaquant.attaque - defenseur.defense 
    return max(10, base)


def tour_de_jeu(joueur, ennemi, joueur_est_humain=True, action=None):
    log = ""
    # Choix des actions
    if joueur_est_humain:
        if action == "attaquer":
            action_joueur = "attaquer"
        elif action == "defendre":
            action_joueur = "defendre"
    else:
        action_joueur = random.choice(["attaquer", "defendre"])

    
    # Appliquer défense (avant d'être attaqué)
    if action_joueur == "defendre":
        joueur.en_defense = True
        log += f"{joueur.nom} se prépare à encaisser les coups.\n"
    else:
        joueur.en_defense = False
        degats = calcul_degats(joueur, ennemi)
        ennemi.prendre_degats(degats)
        log += f"{joueur.nom} attaque {ennemi.nom} et inflige {degats} dégâts !\n"
        log += f"{ennemi.nom} a {ennemi.hp} HP restants.\n"
    return log


   
    
   



