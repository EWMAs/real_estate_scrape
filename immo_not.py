"""Script to scrape houses for sale on immobilier.notaires.fr"""

## Import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time # To pause between actions when using Selenium
from datetime import date # To add date when data is extracted
import gspread # Library to interact with Google Spreadsheets
from oauth2client.service_account import ServiceAccountCredentials # To access Google Account
from pprint import pprint # To pretty print json info in a more readable format
import json
import re



testurl = "https://www.immobilier.notaires.fr/fr/annonces-immobilieres-liste?surfaceMin=100&typeBien=MAI&typeTransaction=VENTE&page=1&parPage=12&tri=PRIX_ASC&prixMin=35000&prixMax=70000&departement=16,17"

start_url = "https://www.immobilier.notaires.fr/fr/annonces-immobilieres-liste"
surfaceMin = 100
typeBien = "MAI"
typeTransaction = "VENTE"
prixMin=35000
prixMax=70000
departement="14,27,28,45,50,78,89"

results_url = f"{start_url}?surfaceMin={surfaceMin}&typeBien={typeBien}&typeTransaction={typeTransaction}&prixMin={prixMin}&prixMax={prixMax}&departement={departement}"
#print(results_url)


#Section A – I'm able to navigate to the website, 


#Extract results from page
def parse_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #print(response.text, soup)
    return soup


def extract_house_urls():
    soup = parse_html(results_url)
    links = soup.find_all("a")
    for link in links:
        link = link.get('href')
        print(link)

extract_house_urls()

