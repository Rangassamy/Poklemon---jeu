import time
import random


class Poklemon:
    def __init__(self, nom, type_, hp, attaque, defense, vitesse):
        self.nom = nom
        self.type = type_
        self.hp = hp
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse
        self.en_defense = False  # état actif pour le tour

    def is_alive(self):
        return self.hp > 0

    def prendre_degats(self, degats):
        if self.en_defense:
            degats = degats // 2
        self.hp -= degats
        if self.hp < 0:
            self.hp = 0

    def __str__(self):
        return f"{self.nom} [{self.type}] HP:{self.hp} ATQ:{self.attaque} DEF:{self.defense} VIT:{self.vitesse}"


def calcul_degats(attaquant, defenseur):
    base = attaquant.attaque - defenseur.defense
    return max(1, base)


def tour_de_jeu(joueur, ennemi, joueur_est_humain=True):
    # Choix des actions
    if joueur_est_humain:
        print("\nChoisis ton action :")
        print("1 - Attaquer")
        print("2 - Défendre")
        choix = input("Ton choix : ")
        if choix == "1":
            action_joueur = "attaquer"
        elif choix == "2":
            action_joueur = "defendre"
        else:
            print("Choix invalide. Tu défends par défaut.")
            action_joueur = "defendre"
    else:
        action_joueur = random.choice(["attaquer", "defendre"])

    # Annonce des actions
    print(f"{joueur.nom} choisit : {action_joueur}")

    # Appliquer défense (avant d'être attaqué)
    if action_joueur == "defendre":
        joueur.en_defense = True
    else:
        joueur.en_defense = False

    # Attaque si action = attaquer
    if action_joueur == "attaquer":
        degats = calcul_degats(joueur, ennemi)
        ennemi.prendre_degats(degats)
        print(f"{joueur.nom} attaque {ennemi.nom} et inflige {degats} dégâts !")
        print(f"{ennemi.nom} a {ennemi.hp} HP restants.")
        time.sleep(0.5)
    else:
        print(f"{joueur.nom} se prépare à encaisser les coups.")
        time.sleep(0.5)


def combat(p1, p2):
    print("=== Début du combat ===")
    print(f"{p1.nom} VS {p2.nom}")
    time.sleep(1)

    if p1.vitesse >= p2.vitesse:
        tour_joueur = p1
        tour_bot = p2
        humain_en_premier = True
    else:
        tour_joueur = p2
        tour_bot = p1
        humain_en_premier = False

    tour = 1
    while p1.is_alive() and p2.is_alive():
        print(f"\n-- Tour {tour} --")
        if humain_en_premier:
            tour_de_jeu(tour_joueur, tour_bot, joueur_est_humain=True)
            if tour_bot.is_alive():
                tour_de_jeu(tour_bot, tour_joueur, joueur_est_humain=False)
        else:
            tour_de_jeu(tour_bot, tour_joueur, joueur_est_humain=False)
            if tour_joueur.is_alive():
                tour_de_jeu(tour_joueur, tour_bot, joueur_est_humain=True)

        tour += 1

    print("\n=== Fin du combat ===")
    if p1.is_alive():
        print(f"{p1.nom} a gagné !")
    else:
        print(f"{p2.nom} a gagné !")


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



