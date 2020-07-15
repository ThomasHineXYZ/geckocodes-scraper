#!/usr/bin/env python

import requests;
import urllib.request;
import time;
from bs4 import BeautifulSoup;

# URL to scrape
url = "https://www.geckocodes.org/index.php?chid=R&r=*&l=all";

# Connect to the URL
response = requests.get(url);

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser");

for link in soup.find("div", class_="list").findAll("a"):
    print(link.get('href'))
    time.sleep(0.5);
