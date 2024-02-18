
import requests
from bs4 import BeautifulSoup
from pprint import pprint



url = "https://books.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# We want to have all the names of the categories in the sidebar on the page

aside = soup.find("div", {"class": "side_categories"})

categories_div = aside.find("ul").find("li").find("ul")

categories = [child.text.strip()
              for child in categories_div.children if child.name]
# print(categories)


# for category in categories.children:
#     if category.name:
#         print(category.text.strip())

# Now we want to get some attributes from html elements images for example the attribute "src"

images_section = soup.find("section").find_all("img")

images =[image["src"] for image in images_section ]
# print("\nImages:\n")

# for image in images:
#     print(image.get("src"))

# Now we want to get the titles of the books, the title is found in the second
#tag a inside an article with a class "product_pod", found all the article by his class, the second tag <a>
#and the title of the books is in the attribute "title" of the <a> tag
# then we display the title by the method .get('title'), it gives None if the attribute is not found.

#Method 1:
# articles = soup.find_all("article", class_="product_pod")
# for article in articles:
#     links = article.find_all("a") # Get all the <a> tag inside the article
#     if len(links)>= 2:
#         link=links[1]
#         print(link.get('title'))

#Method 2:

# titles_tag = soup.find_all('a', title= True)
# titles = [title.get('title') for title in titles_tag]
# titles = [a['title'] for a in titles_tag]
titles = [a['title'] for a in soup.find_all('a', title= True)] # one line code
pprint(titles)
