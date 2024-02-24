import requests
from bs4 import BeautifulSoup



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
        one_star_books = soup.select(".star-rating.One")
        print(len(one_star_books))
        
    
    
    

    










if __name__ == '__main__':
    main()
    
# 1. Get the HTML