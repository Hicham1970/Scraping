import requests
from bs4 import BeautifulSoup

# url="https://books.toscrape.com"
# response = requests.get(url)
# soupe = BeautifulSoup(response.text, 'html.parser')
# print(soupe.prettify() )  # to print the whole HTML content of the webpage in a pretty format







response = requests.get('https://www.google.com')

print(response.status_code)
#create a file to store the html content of web page in it :
with open('google.html', 'w') as f:
    f.write(response.text)
    # f.write(response.json) if we want to convert to json