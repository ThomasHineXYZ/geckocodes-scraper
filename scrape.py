#!/usr/bin/env python

from bs4 import BeautifulSoup;
import os;
import tarfile;
import tempfile;
import time;
import urllib.request

# URLs to scrape
urls = {
    # 'Wii': {
    #     'fileName': 'wii',
    #     'url': 'https://www.geckocodes.org/index.php?chid=R&r=*&l=all'
    # },
    # 'WiiWare': {
    #     'fileName': 'wii_ware',
    #     'url': 'https://www.geckocodes.org/index.php?chid=W&r=*&l=all'
    # },
    # 'Virtual Console Arcade': {
    #     'fileName': 'virtual_console_arcade',
    #     'url': 'https://www.geckocodes.org/index.php?chid=D&r=*&l=all'
    # },
    'Wii Channels': {
        'fileName': 'wii_channels',
        'url': 'https://www.geckocodes.org/index.php?chid=H&r=*&l=all'
    },
    # 'Gamecube': {
    #     'fileName': 'gamecube',
    #     'url': 'https://www.geckocodes.org/index.php?chid=G&r=*&l=all'
    # },
    # 'NES / Famicom': {
    #     'fileName': 'n_e_s_famicom',
    #     'url': 'https://www.geckocodes.org/index.php?chid=F&r=*&l=all'
    # },
    # 'Super NES/Famicom': {
    #     'fileName': 'super_n_e_s_famicom',
    #     'url': 'https://www.geckocodes.org/index.php?chid=J&r=*&l=all'
    # },
    # 'Nintendo 64': {
    #     'fileName': 'nintendo_64',
    #     'url': 'https://www.geckocodes.org/index.php?chid=N&r=*&l=all'
    # },
    # 'Sega Master System': {
    #     'fileName': 'sega_master_system',
    #     'url': 'https://www.geckocodes.org/index.php?chid=L&r=*&l=all'
    # },
    # 'Genesis/Mega Drive': {
    #     'fileName': 'genesis_mega_drive',
    #     'url': 'https://www.geckocodes.org/index.php?chid=M&r=*&l=all'
    # },
    # 'NeoGeo': {
    #     'fileName': 'neo_geo',
    #     'url': 'https://www.geckocodes.org/index.php?chid=E&r=*&l=all'
    # },
    # 'Commodore 64': {
    #     'fileName': 'commodore_64',
    #     'url': 'https://www.geckocodes.org/index.php?chid=C&r=*&l=all'
    # },
    # 'MSX': {
    #     'fileName': 'msx',
    #     'url': 'https://www.geckocodes.org/index.php?chid=X&r=*&l=all'
    # },
    # 'TurboGraFX-16': {
    #     'fileName': 'turbo_gra_f_x_16',
    #     'url': 'https://www.geckocodes.org/index.php?chid=P&r=*&l=all'
    # },
    # 'TurboGraFX-CD': {
    #     'fileName': 'turbo_gra_f_x_c_d',
    #     'url': 'https://www.geckocodes.org/index.php?chid=Q&r=*&l=all'
    # },
};

txtDownloadUrl = "https://www.geckocodes.org/txt.php?txt=";

for url in urls:
    # Connect to the URL
    response = urllib.request.urlopen(urls[url]['url']).read();

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response, "html.parser");

    # Create a temporary directory
    tempDirectory = tempfile.TemporaryDirectory();

    # Iterate through each of the games listed
    for link in soup.find("div", class_="list").findAll("a"):
        # Grab just the hyperlink, since thats all we are interested in
        cheatLink = link.get('href');

        # Chop off the index.php part
        titleId = cheatLink.replace("./index.php?c=", "");

        # Finally save the resulting text file
        response = urllib.request.urlretrieve(txtDownloadUrl + titleId, tempDirectory.name + "/" + titleId + ".txt");

    # Put all of the newly downloaded files in to a tar.gz archive file
    tar = tarfile.open(urls[url]['fileName'] + ".tar.gz", "w:gz");
    for name in os.listdir(tempDirectory.name):
        tar.add(tempDirectory.name + "/" + name, arcname=name);
    tar.close();

    # Close the temp directory to clean up the files
    tempDirectory.cleanup();
