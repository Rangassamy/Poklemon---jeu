from random import *
import pygame
import requests
from io import BytesIO
import asyncio
from playwright.async_api import async_playwright

#executable_path="C:/Users/Temp/Desktop/chromium-win64/chrome-win/chrome.exe"
async def get_all_names():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://infinitefusion.online/?")

        # Extraction des noms
        all_names = []
        elements = await page.query_selector_all("#FirstPokemonDatalist > option")
        for i, element in enumerate(elements):
            text = await element.inner_text()
            all_names.append(text.split(" ")[1])

        await browser.close()
        return(all_names)
    
async def get_fusion_info(a, b):
    # Extration de l'image
    url = "https://cdn.jsdelivr.net/gh/fusiondex-org/infinite-fusion-graphics/custom/"+str(a)+"."+str(b)+".png"
    response = requests.get(url)
    URL = "https://infinitefusion.online/?firstpoke="+list_all_names[a-1]+"&secondpoke="+list_all_names[b-1]
    if response.status_code != 200:
        url = "https://cdn.jsdelivr.net/gh/fusiondex-org/infinite-fusion-graphics/custom/"+str(b)+"."+str(a)+".png"
        response = requests.get(url)
        URL = "https://infinitefusion.online/?firstpoke="+list_all_names[b-1]+"&secondpoke="+list_all_names[a-1]
        if response.status_code != 200:
            url = "https://cdn.jsdelivr.net/gh/fusiondex-org/infinite-fusion-graphics/autogen/"+str(a)+"/"+str(a)+"."+str(b)+".png"
            response = requests.get(url)
            URL = "https://infinitefusion.online/?firstpoke="+list_all_names[a-1]+"&secondpoke="+list_all_names[b-1]
    image_data = BytesIO(response.content)
    print("image recupere")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(URL)

        # Extraction du nom
        name = await page.inner_text('#PokemonOneName')
        name = name.split(':')[0]

        _type = ""
        elements = await page.query_selector_all("#PokemonOneTypes > div")
        for i, element in enumerate(elements):
            text = await element.inner_text()
            _type = _type + text + " "
        _type = _type[:-1]

        # Extraction des stats
        stat = []
        pv_element = await page.query_selector("#PokemonOneHP")
        pv = await pv_element.inner_text()
        stat.append(int(pv.split(" ")[0]))

        pv_element = await page.query_selector("#PokemonOneAttack")
        pv = await pv_element.inner_text()
        stat.append(int(pv.split(" ")[0]))

        pv_element = await page.query_selector("#PokemonOneDefense")
        pv = await pv_element.inner_text()
        stat.append(int(pv.split(" ")[0]))

        pv_element = await page.query_selector("#PokemonOneSpeed")
        pv = await pv_element.inner_text()
        stat.append(int(pv.split(" ")[0]))


        # Extraction des attacks
        all_attacks = []
        elements = await page.query_selector_all("#PokemonOneAbility > div")
        for i, element in enumerate(elements):
            if i < 3:
                all_attacks.append(await element.inner_text())

        await browser.close()
        return(name, _type, stat, all_attacks, image_data)


list_all_names = asyncio.run(get_all_names())
print("nom recuperer")

a = randint(0, 501)
b = randint(0, 501)
print(a, b)

fusion_info = asyncio.run(get_fusion_info(a, b))
nom_fusion = fusion_info[0]
poke_type = fusion_info[1]
stat = fusion_info[2]
all_attack = fusion_info[3]
image_data = fusion_info[4]

#Création de la fenêtre
pygame.init()
width, height = 400, 455
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(str(a)+"x"+str(b))

#Affichage
screen.fill((255, 255, 255))
pygame.draw.rect(screen, (64, 64, 64), pygame.Rect(56, 40, 288, 288))
image = pygame.image.load(image_data)
screen.blit(image, (31, 40))
font=pygame.font.Font(None,30)

nom_text=font.render(nom_fusion, 1,(0,0,0))
nom_text_rect = nom_text.get_rect(center=(width//2, 20))
screen.blit(nom_text, nom_text_rect)

type_text=font.render(poke_type, 1, (0, 0, 0))
type_text_rect = type_text.get_rect(center=(width//2, 348))
screen.blit(type_text, type_text_rect)

stat_text=font.render("HP : "+str(stat[0])+", Attack : "+str(stat[1]), 1,(0,0,0))
stat_text_rect = stat_text.get_rect(center=(width//2, 380))
screen.blit(stat_text, stat_text_rect)
stat_text=font.render("Defense : "+str(stat[2])+", Speed : "+str(stat[3]), 1,(0,0,0))
stat_text_rect = stat_text.get_rect(center=(width//2, 400))
screen.blit(stat_text, stat_text_rect)

attack_text=font.render(all_attack[0]+" | "+all_attack[1]+" | "+all_attack[2], 1, (0, 0, 0))
attack_text_rect = attack_text.get_rect(center=(width//2, 440))
screen.blit(attack_text, attack_text_rect)

pygame.display.flip()

#Boucle d'attente
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
