#!/usr/bin/env python

import requests;
import time;
from bs4 import BeautifulSoup;

# URLs to scrape
urls = {
    'Wii': {
        'folder': 'wii',
        'url': 'https://www.geckocodes.org/index.php?chid=R&r=*&l=all'
    },
    'WiiWare': {
        'folder': 'wii_ware',
        'url': 'https://www.geckocodes.org/index.php?chid=W&r=*&l=all'
    },
    'Virtual Console Arcade': {
        'folder': 'virtual_console_arcade',
        'url': 'https://www.geckocodes.org/index.php?chid=D&r=*&l=all'
    },
    'Wii Channels': {
        'folder': 'wii_channels',
        'url': 'https://www.geckocodes.org/index.php?chid=H&r=*&l=all'
    },
    'Gamecube': {
        'folder': 'gamecube',
        'url': 'https://www.geckocodes.org/index.php?chid=G&r=*&l=all'
    },
    'NES / Famicom': {
        'folder': 'n_e_s_famicom',
        'url': 'https://www.geckocodes.org/index.php?chid=F&r=*&l=all'
    },
    'Super NES/Famicom': {
        'folder': 'super_n_e_s_famicom',
        'url': 'https://www.geckocodes.org/index.php?chid=J&r=*&l=all'
    },
    'Nintendo 64': {
        'folder': 'nintendo_64',
        'url': 'https://www.geckocodes.org/index.php?chid=N&r=*&l=all'
    },
    'Sega Master System': {
        'folder': 'sega_master_system',
        'url': 'https://www.geckocodes.org/index.php?chid=L&r=*&l=all'
    },
    'Genesis/Mega Drive': {
        'folder': 'genesis_mega_drive',
        'url': 'https://www.geckocodes.org/index.php?chid=M&r=*&l=all'
    },
    'NeoGeo': {
        'folder': 'neo_geo',
        'url': 'https://www.geckocodes.org/index.php?chid=E&r=*&l=all'
    },
    'Commodore 64': {
        'folder': 'commodore_64',
        'url': 'https://www.geckocodes.org/index.php?chid=C&r=*&l=all'
    },
    'MSX': {
        'folder': 'msx',
        'url': 'https://www.geckocodes.org/index.php?chid=X&r=*&l=all'
    },
    'TurboGraFX-16': {
        'folder': 'turbo_gra_f_x_16',
        'url': 'https://www.geckocodes.org/index.php?chid=P&r=*&l=all'
    },
    'TurboGraFX-CD': {
        'folder': 'turbo_gra_f_x_c_d',
        'url': 'https://www.geckocodes.org/index.php?chid=Q&r=*&l=all'
    },
};

for url in urls:
    # Connect to the URL
    response = requests.get(urls[url]['url']);

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser");

    for link in soup.find("div", class_="list").findAll("a"):
        # print(link.get('href'));
        print(link.get('title'));
        # time.sleep(0.5); # For testing
