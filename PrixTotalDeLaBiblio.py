import sys
from typing import List
import re

from selectolax.parser import HTMLParser
from loguru import logger
import requests


logger.remove()
logger.add(f'books.log', rotation="500kb", level="WARNING")
logger.add(sys.stderr, level="INFO")



def get_all_books_urls(url: str) -> list[str]:
    """
    But : Récupérer toutes les urls des livres sur la bibliothèque
    Args: url (str): L'url de depart
    Returns:list[str]: Liste de toutes les urls de toutes les pages
    """
    pass


def get_next_page(tree: HTMLParser) -> str:
    """
     But : Récupérer l'url de la page suivante a partir du html d'une page donnée
     Args:tree : Objet HTMLParser contenant le code html d'une page
     Returns : str: Url de la page suivante
    """
    pass


def get_all_books_url(tree: HTMLParser, page_number: int) -> List:
    """
    But: Récupére les urls de tous les livres sur une page donnée
     Args:tree : Objet HTMLParser contenant le code html d'une page
     Returns : str[url]:Liste des  Urls de tous les livres de la page 
    """
    pass



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
        logger.error("No price node found")
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
    return 1


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
    url="https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    get_book_price(url=url)


#* Functions to code:
#! Fonction pour récupérer l'url de la page suivante
# ?     - Récupérer a partir de HTML ou de l'url??
#!  Fonction qui a parir de l'url d'un livre va calculer le prix total:
# ?     - Fonction pour récupérer le prix de l'article a partir du Html
# ?     - Fonction pour récupérer la quantité disponible a partir du Html
#!  Fonction pour récupérer les urls de tous les livres de la bibliothèque.
#!  Fonction pour récupérer les Urls sur une page spécifique.
