import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
}
word = input("Word:")
url = 'http://www.oxfordlearnersdictionaries.com/us/definition/english/' + word
response = requests.get(url, headers=headers)
content = BeautifulSoup(response.content, 'html.parser')
defs = content.find_all('span', class_="shcut")

for d in defs:
    print(d.get_text())
