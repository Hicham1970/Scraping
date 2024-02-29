import sys
from typing import List

from selectolax.parser import HTMLParser
from loguru import logger

logger.remove()
logger.add(f'books.log', rotation="500kb", level="WARNING")
logger.add(sys.stderr, level="INFO")


"""
# Fonction pour récupérer les urls de tous les livres de la bibliothèque.
# Fonction pour récupérer l'url de la page suivante  
# Fonction pour récupérer les Urls sur une page spécifique.
"""

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


def get_all_books_url(tree:HTMLParser, page_number:int)->List:
    """
    But: Récupére les urls de tous les livres sur une page donnée
     Args:tree : Objet HTMLParser contenant le code html d'une page
     Returns : str[url]:Liste des  Urls de tous les livres de la page 
    """    
    pass



def get_book_price_based_on_quantity(url: str) -> float:
    """
    But : Récupére le prix d'un livre à partir de son url
    Args: url (str):url de la page du live
    Returns: float: Prix du livre multiplié par le nombre d'exemplaires disponibles
    """    
    pass


def extract_price_from_page(tree: HTMLParser) -> float:
    """
    But : Récupére le prix d'un livre à partir du code html de sa page
    Args:tree (HTMLParser): Objet HTMLParser contenant le code html de la page du livre
    Returns: float: le prix unitaire du livre
    """    
    pass








def main(){
    pass
}







if __name__ =='__main__':
    main()
    
    
    
    
    
    
"""
Functions to code:
* Fonction pour récupérer l'url de la page suivante
    - Récupérer a partir de HTML ou de l'url??
* Fonction qui a parir de l'url d'un livre va calculer le prix total:
    - Fonction pour récupérer le prix de l'article a partir du Html
    - Fonction pour récupérer la quantité disponible a partir du Html
* Fonction pour récupérer les urls de tous les livres de la bibliothèque.
* Fonction pour récupérer les Urls sur une page spécifique. 
"""

    