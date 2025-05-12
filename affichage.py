import pygame
import json
import os
import requests
from io import BytesIO

# --- Configuration ---
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600
CARD_WIDTH, CARD_HEIGHT = 260, 320
PADDING = 20
CACHE_DIR = "cache"
COLUMNS = 3
SCROLL_SPEED = 30

# --- Initialisation ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokédex Scroll")
font = pygame.font.SysFont(None, 20)

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# --- Chargement des données ---
def load_pokemons(filepath="pokemons_base.jsonl"):
    pokemons = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            pokemons.append(json.loads(line))
    return pokemons

pokemons = load_pokemons()

# --- Chargement image avec cache ---
def get_pokemon_image(pokemon):
    filename = os.path.join(CACHE_DIR, f"{pokemon['index']}.png")
    if not os.path.exists(filename):
        response = requests.get(pokemon["image_url"])
        with open(filename, "wb") as f:
            f.write(response.content)
    img = pygame.image.load(filename)
    return pygame.transform.scale(img, (100, 100))

# --- Affichage d'une carte ---
def draw_card(pokemon, x, y):
    pygame.draw.rect(screen, (240, 240, 240), (x, y, CARD_WIDTH, CARD_HEIGHT))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), 2)

    img = get_pokemon_image(pokemon)
    screen.blit(img, (x + (CARD_WIDTH - 100) // 2, y + 10))

    def txt(s, dy): return font.render(s, True, (0, 0, 0)), (x + 10, y + dy)
    name = f"{pokemon['index']}. {pokemon['name']}"
    screen.blit(*txt(name, 120))
    screen.blit(*txt("Types: " + ", ".join(pokemon['types']), 150))

    stats = pokemon['stats']
    screen.blit(*txt(f"HP:{stats['hp']} ATK:{stats['attack']}", 180))
    screen.blit(*txt(f"DEF:{stats['defense']} SPD:{stats['speed']}", 200))

    attacks = " | ".join(pokemon["attacks"])
    screen.blit(*txt(attacks, 230))

# --- Boucle principale ---
clock = pygame.time.Clock()
scroll_y = 0
max_scroll = ((len(pokemons) + COLUMNS - 1) // COLUMNS) * (CARD_HEIGHT + PADDING) - SCREEN_HEIGHT

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            scroll_y -= event.y * SCROLL_SPEED
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                scroll_y -= SCROLL_SPEED
            elif event.key == pygame.K_UP:
                scroll_y += SCROLL_SPEED
            elif event.key == pygame.K_ESCAPE:
                running = False

    scroll_y = max(min(scroll_y, 0), -max_scroll)

    # Afficher les cartes
    for idx, pokemon in enumerate(pokemons):
        row = idx // COLUMNS
        col = idx % COLUMNS
        x = PADDING + col * (CARD_WIDTH + PADDING)
        y = PADDING + row * (CARD_HEIGHT + PADDING) + scroll_y
        if -CARD_HEIGHT < y < SCREEN_HEIGHT:
            draw_card(pokemon, x, y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
