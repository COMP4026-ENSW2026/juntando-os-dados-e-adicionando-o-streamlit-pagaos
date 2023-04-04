import requests
from bs4 import BeautifulSoup
import json
import re

URL = 'https://www.auroraimobi.com.br/imoveis/para-alugar/apartamento/londrina-pr?mobilia=talvez&condominio=&order=mais_relevantes'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

cards = soup.find_all('li', class_='Imoveis_cardDisplay__e0Dc8')

properties = []
titles = []
links = []
rooms = []
bathrooms = []
sizes = []
locations = []

for card in cards:
    title = card.find('span', class_='font-weight-bold')
    link = card.find('a')
    immobile = card

    titles.append(title.text.strip())
    links.append('https://www.auroraimobi.com.br' + link['href'])
    properties.append(immobile)


def get_details_page(aparment_url):
    details_page = requests.get(aparment_url)
    soup = BeautifulSoup(details_page.content, 'html.parser')

    aparment_characteristics = soup.find_all(
        'span', class_='Caracteristica_title__vzVJS')
    
    aparment_locations = soup.find_all('address', class_='mb-1', itemprop='address')
    
    for location in aparment_locations:
        locations.append(location.text.strip())

    results = []
    for characteristic in aparment_characteristics:
        value = re.findall(r'\d+', characteristic.text)
        results.append(value[0] if value else None)

    rooms.append(results[0])
    bathrooms.append(results[1])
    sizes.append(results[2])


for link in links:
    details = get_details_page(link)

print(titles)
print(locations)
print(rooms)
print(bathrooms)
print(sizes)
print(links)

characteristics = ['titulo', 'localizacao', 'quartos', 'banheiros',
                   'tamanho', 'aluguel', 'condominio', 'contato', 'link']

json_object = json.dumps(dict(zip(titles, links)), ensure_ascii=False)
