import requests
from bs4 import BeautifulSoup
from pprint import pprint


url="https://books.toscrape.com"
response = requests.get(url, timeout=5)


soupe = BeautifulSoup(response.text, 'html.parser')
# print(soupe.prettify() )  # to print the whole HTML content of the webpage in a pretty format

#To print all the images in the script using the biblio pprint
# images = soupe.find_all('img')
# pprint(images)


# to get all the articles with the class name "product_pod":

# articles = soupe.find_all('article', class_="product_pod")
# pprint(articles)

# to get the aside:
aside = soupe.find('aside', class_="sidebar")

# for child in aside.children:
#     if child.name :
#         print("Child Name: ",child.name)


# to get the div with the class aside-categories inside the aside  element and then find all the <a> tags within it:

asideCategories = aside.find('div', class_="side_categories")
# h3 = asideCategories.find_all('h3')
ul = asideCategories.find('ul')
li = ul.find_all('li')


# print(asideCategories.prettify())
# print(li)

# to get all the <a> tags within the aside element:
categoryLinks = li[0].find_all('a')   # it will return like aside.find_all('a')
pprint(categoryLinks)

# links = aside.find_all('a')
# pprint(links)