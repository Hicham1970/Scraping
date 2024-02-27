import requests
from bs4 import BeautifulSoup


# Recuperer toutes les pages :
def get_All_Pages():
    urls = []
    page_number = 1

    for i in range(151):
        i = f"https://www.dabadoc.com/ma/medecin-generaliste/casablanca/page/{
            page_number}"
        page_number += 1
        urls.append(i)

    return urls

# get_All_Pages()


def get_Medecins():
    re = requests.get(
        'https://www.dabadoc.com/ma/medecin-generaliste/casablanca/page/1', timeout=5)
    soup = BeautifulSoup(re.content, "html.parser")

    medecins = soup.find_all('div', class_='result-box rounded')
    # print(len(medecins))  # nombre de médecins dans la page 15
    # Pour récupérer les informations d'un médecin, on va utiliser la fonction find_all()

    for medecin in medecins:
        try:
            nom = medecin.find("h2").text.strip()
        except AttributeError as e: 
            nom = " " + str(e)

        try:
            specialité = medecin.find("p").text.strip()
        except AttributeError as e:
            specialité = " "   + str(e) 

        try:
            quartier = medecin.find("span")
        except AttributeError as err:
            quartier = " " + str(err)    
        print(quartier.text)
    
        # new url
        # new_url = "https://www.dabadoc.com/ma/diabetologue/casablanca/ouafae-guessous-krafess"

        print(nom, specialité, quartier)


get_Medecins()
