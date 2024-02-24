import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/index.html"


def main(threshold: int=5):
    """Scrapes the books from the toscrape website and prints out any book"""
    with requests.Session() as session:
        response = session.get(BASE_URL, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup.prettify())
        # categories = soup.find("ul", class_="nav nav-list").find_all("a")

        #Alternative
        categories = soup.select("ul.nav.nav-list a")
        #  we want to get the url inside the tag <a>, we use the loop with the
        # the comprehension list method and targetting the href attribute

        # categories = [category['href'] for category in categories]
        # categories = [category.get("href").strip() for category in categories]
        # categories = [category.text.strip() for category in categories[1:]]
        categories_url = [category["href"] for category in categories[1:]]

        for category_url in categories_url:
            full_url = urljoin(BASE_URL, category_url)
            response = session.get(full_url, timeout=5)
        
        response = session.get(BASE_URL, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser") 
        # print(soup.prettify())
        # categories = soup.find("ul", class_="nav nav-list").find_all("a")

        #Alternative
        categories = soup.select("ul.nav.nav-list a")
        #  we want to get the url inside the tag <a>, we use the loop with the 
        # the comprehension list method and targetting the href attribute
        
        # categories = [category['href'] for category in categories]
        # categories = [category.get("href").strip() for category in categories]
        # categories = [category.text.strip() for category in categories[1:]]
        categories_url = [category["href"] for category in categories[1:]]

        for category_url in categories_url:
            full_url = urljoin(BASE_URL, category_url)
            response = session.get(full_url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.select("article.product_pod")
            # print(f"Books in {category_url}: {len(books)}")
            number_of_books = len(books)
            categoruy_title = soup.select_one("h1").text
            
            if number_of_books <= threshold:
                print(f"The category '{categoruy_title}' has only {number_of_books} books .")
            
            else:
                print(f"The category '{categoruy_title}' has enough books : {number_of_books} books  .")
                








if __name__ == '__main__':
    main(threshold=5)





