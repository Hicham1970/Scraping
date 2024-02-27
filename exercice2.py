import requests
from bs4 import BeautifulSoup
import re


url = "https://books.toscrape.com"

def main():
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise exception if status is not 
    except requests.exceptions.RequestException as err:
        print(f"Il y a eu un problème avec la requête: {err}")
        raise requests.exceptions.RequestException from err
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        one_star_books = soup.select("p.star-rating.One")
        # print(len(one_star_books))
        # la deuxiéme partie de l'exercice est de recuperer le numero de chaque 
        # livre , il se trouve dans un <a> qui se trouve dans <h3> juste apres le <p>
        # avec la class  star-rating One;
        
        for book in one_star_books:
            # title = book.find_next_sibling("h3").find("a").get('title')
            try:
                book_link = book.find_next_sibling("h3").find("a")["href"]
                print(book_link)
            except AttributeError as e :
                print("Impossible de troouver la balise'<h3>'")
                raise  AttributeError from e
            except TypeError as e :
                print("Impossible de trouver la balise '<a>'")
                raise  TypeError from e
            except KeyError as e :
                print("Impossible de trouver l'attribut 'href'")
                raise  KeyError from e
    
    
    

    










if __name__ == '__main__':
    main()
    
    
    