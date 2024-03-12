import sys
from typing import List
import re
from urllib.parse import urljoin

from selectolax.parser import HTMLParser
from loguru import logger
import requests


logger.remove()
logger.add(f'books.log', rotation="500kb", level="WARNING")
logger.add(sys.stderr, level="INFO")

Url_De_Base ="https://books.toscrape.com/index.html"

def get_all_books_urls(url: str) -> list[str]:
    """
    But : Récupérer toutes les urls des livres sur la bibliothèque
    Args: url (str): L'url de depart
    Returns:list[str]: Liste de toutes les urls de toutes les pages
    """
    pass


def get_next_page_url(tree: HTMLParser) -> str:
    """
     But : Récupérer l'url de la page suivante a partir du html d'une page donnée
     Args:tree : Objet HTMLParser contenant le code html d'une page
     Returns : str: Url de la page suivante
    """
    pass


def get_all_books_urls_on_page(tree: HTMLParser) -> List:
    """
    But: Récupére les urls de tous les livres sur une page donnée
     Args:tree : Objet HTMLParser contenant le code html d'une page
     Returns : str[url]:Liste des  Urls de tous les livres de la page 
    """
    try:
        books_links_nodes = tree.css("h3 > a")
        return [urljoin(Url_De_Base, link.attributes["href"]) for link in books_links_nodes if "href" in link.attributes] # selectionne tout les noeuds qui ont un attribut href # selectionne tout les noeuds qui ont un attribut href
        
    except Exception as e:
        logger.error(f"Erreur lors de k'extraction des urls des livres : {e}")
        return []
    # print(books_links_nodes[0].attributes["href"])

def get_book_price(url: str) -> float:
    """
    But : 1erement ; Récupére le prix d'un livre à partir de son url
    Args: url (str):url de la page du live
    Returns: float: Prix du livre multiplié par le nombre d'exemplaires disponibles
    """     
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        tree = HTMLParser(res.text)
        print(tree)
        price = extract_price_from_page(tree=tree)
        stock = extract_stock_quantity_from_page(tree=tree)
        return price * stock
    except requests.exceptions.RequestException as e:
        logger.error(f"Error while requesting {url}: {e}")
        return 0.0         # Returning 0.0 to avoid not having a price


def extract_price_from_page(tree: HTMLParser) -> float:
    """
    But :  2ement ; Récupére le prix d'un livre à partir du code html de sa page
    Args:tree (HTMLParser): Objet HTMLParser contenant le code html de la page du livre
    Returns: float: le prix unitaire du livre
    NB: 
    """
    price_node = tree.css_first("p.price_color")
    if price_node:
        price_string = price_node.text()
    else:
        logger.error("Aucun prix n' a été trouvé dans la page")
        return 0.0

    try:
        price = re.findall(r"[0-9.]+", price_string)[0]
    except IndexError as e:
        logger.error(f"Aucun nombre n' a été trouvé dans :  {price_string}: {e}")
        return 0.0
    else:
        print(float(price))
        return float(price)
    
        
        
         
def extract_stock_quantity_from_page(tree: HTMLParser) -> int:
    """
    But : Récupére la quantité disponible en stock d'un livre à partir du code html de sa page
    Args:tree (HTMLParser): Objet HTMLParser contenant le code html de la page du livre
    Returns: int: la quantité disponible du livre
    """
    try:    
        stock_node = tree.css_first("p.instock.availability")
        return int(re.findall(r"[0-9]+", stock_node.text())[0])
    except AttributeError as e:
        logger.error(f"Aucun noeud n' a été trouvé dans la page : {e}")
        return 0
    except IndexError as e:
        logger.error(f"Aucun nombre n' a été trouvé dans le noued : {e}")
        return 0
        


def main():
    base_url = "https://books.toscrape.com/index.html"
    all_books_urls = get_all_books_urls(url=base_url)
    total_ptice = []

    # Récupérer le prix de chaque livre et le sommer pour obtenir le prix total de la bibliothèque.
    for book_url in all_books_urls:
        price = get_book_price(url=book_url)
        total_ptice.append(price)

    return sum(total_ptice)


if __name__ == '__main__':
    r = requests.get(Url_De_Base)
    tree=HTMLParser(r.text)
    get_all_books_urls_on_page(tree=tree) 


#* Functions to code:
#! Fonction pour récupérer l'url de la page suivante
# ?     - Récupérer a partir de HTML ou de l'url??
#!  Fonction qui a parir de l'url d'un livre va calculer le prix total:
# ?     - Fonction pour récupérer le prix de l'article a partir du Html
# ?     - Fonction pour récupérer la quantité disponible a partir du Html
#!  Fonction pour récupérer les urls de tous les livres de la bibliothèque.
#!  Fonction pour récupérer les Urls sur une page spécifique.
