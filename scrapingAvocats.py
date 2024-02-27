import re
import requests
from bs4 import BeautifulSoup


# But: Scraping an Avocat Web page/site
# We need to find the right selectors for the avocats.
# on va utiliser 3 fonctions,  la 1ere pour recuperer les urls, la 2eme pour parser la 1ere page, et la 3 eme va utiliser
# les urls pour recuperer les infos de chaque avocat de chacune des 104 pages
# on va corriger les adresses des avocats par le billet des Regex  de Python en remplacant les espaces inutiles
# une fois les infos de la premiére page sont collectés, on va les sauvegarder
# dans un fichier txt, et par la suite automatiser le processus aux autres pages.
# on va creer un fichier txt dont l'adresse est chemain


# Noter que ce site contient 104 pages qui ne différent  que par le nombre de pages qu'on ajoute a la fin de l url

# 1. get_avocats_urls, put all the urls in a List[]

def get_All_Pages():
    urls = []
    page_number = 1

    for i in range(104):
        i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={
            page_number}"
        page_number += 1
        urls.append(i)

    return urls

# get_All_Pages()


# 2. get_avocats_infos a partir d'une page

def get_Avocat(url):
    r = requests.get(
        url, timeout=5)
    soup = BeautifulSoup(r.content, "html.parser")
    # On récupère toutes les div qui contient les infos des avocats
    avocats = soup.find_all("div", class_="callout secondary annuaire-single")
   # Chaque page contient 12 avocats, on peut y louper pour recuperer les infos de chaque avocat:

    for avocat in avocats:
        try:
            nom = avocat.find("h3").text.strip()
        except AttributeError as err:
            nom = " "
        try:
            adresse = avocat.find("span", class_="adresse").text.strip()
        except AttributeError as err:
            adresse = " "
        try:
            adresse_finale = re.sub(r'\s+', ' ', adresse)
        except AttributeError as err:
            adresse_finale = ""
        try:
            telephone = avocat.find("span", class_="telephone").text.strip()
        except AttributeError as err:
            telephone = "" + str(err)
        try:
            email = avocat.find("span", class_="email").a.text.strip()
        except AttributeError as err:
            email = "" + str(err)
        try:
            palmares = avocat.find("span", class_="num-case").text.strip()
        except AttributeError as err:

            palmares = "" + str(err)

        chemin = r"E:\Dev\python_files\Scraping\annuaire_avocats.txt"
        with open(chemin, "a") as f:
            f.write(f"Nom: {nom}" + "\n")
            f.write(f"Adresee: {adresse_finale}" + "\n")
            f.write(f"N° Tel: {telephone}" + "\n")
            f.write(f"Email: {email}" + "\n")
            f.write(f"Palmares: {palmares}" + "\n" + "\n" + "\n")


def get_All_Avocat():
    pages = get_All_Pages()
    for page in pages:
        get_Avocat(url=page)
        print(f"Page gratée N°: {page}")

get_All_Avocat()