import time
# import json
# import random


class Poklemon:
    def __init__(self, nom, type_, hp, attaque, defense, vitesse):
        self.nom = nom
        self.type = type_
        self.hp = hp
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse

    def is_alive(self):
        return self.hp > 0

    def prendre_degats(self, degats):
        self.hp -= degats
        if self.hp < 0:
            self.hp = 0

    def __str__(self):
        return f"{self.nom} [{self.type}] HP:{self.hp} ATQ:{self.attaque} DEF:{self.defense} VIT:{self.vitesse}"


def calcul_degats(attaquant, defenseur):
    base = attaquant.attaque - defenseur.defense
    return max(1, base)


def combat(p1, p2):
    print("=== Début du combat ===")
    print(f"{p1.nom} VS {p2.nom}")
    time.sleep(1)

    if p1.vitesse >= p2.vitesse:
        attaquant, defenseur = p1, p2
    else:
        attaquant, defenseur = p2, p1

    tour = 1
    while p1.is_alive() and p2.is_alive():
        print(f"\n-- Tour {tour} --")
        degats = calcul_degats(attaquant, defenseur)
        defenseur.prendre_degats(degats)
        print(f"{attaquant.nom} attaque {defenseur.nom} et inflige {degats} dégâts !")
        print(f"{defenseur.nom} a {defenseur.hp} HP restants.")
        time.sleep(0.5)

        attaquant, defenseur = defenseur, attaquant
        tour += 1

    print("\n=== Fin du combat ===")
    if p1.is_alive():
         print(f"{p1.nom} a gagné !")
       
    else:
         print(f"{p2.nom} a gagné !")
       

# Chargement du fichier JSON
# with open("/data/pokemons_base.jsonl", "r") as f:
#     data = json.load(f)

# # Tirer deux poklemon différents au hasard
# p1_data, p2_data = random.sample(data, 2)



p1 = {
    "nom": "Amaura",
    "type_": "ROCK/ICE",
    "hp": 77,
    "attaque": 59,
    "defense": 50,
    "vitesse": 46
}

p2 = {
    "nom": "Aurorus",
    "type_": "ROCK/ICE",
    "hp": 123,
    "attaque": 77,
    "defense": 72,
    "vitesse": 58
}



