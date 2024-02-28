from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup
import sys
from loguru import logger
import requests


logger.remove()
logger.add("books.log", rotation="500kb", level="WARNING")
logger.add(sys.stderr, level="INFO")

url = "https://books.toscrape.com/index.html"
re = requests.get(url)

tree = HTMLParser(re.text)
soup = BeautifulSoup(re.text, "html.parser")


all_links_soup = soup.select("a")
first_link_soup = soup.select_one("a")

all_link_tree = tree.css("a")
first_link_tree = tree.css_first("a")


print(all_link_tree)
