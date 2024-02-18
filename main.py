import requests
from bs4 import BeautifulSoup


BASE_URL = "https://books.toscrape.com/index.html"


def main():
    response = requests.get(BASE_URL, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser") 
    print(soup.prettify())
    # categories = soup.find("ul", class_="nav nav-list").find_all("a")

     #Alternative
    categories = soup.select("ul.nav.nav-list a")
    print(categories)









if __name__ == '__main__':
    main()





