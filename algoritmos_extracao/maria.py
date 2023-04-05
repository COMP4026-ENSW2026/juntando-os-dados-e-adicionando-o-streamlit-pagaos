import os.path
import requests
from bs4 import BeautifulSoup
import json
import re
import os
from mount_json import mount_json

URL = "https://www.auroraimobi.com.br/imoveis/para-alugar/apartamento/londrina-pr?mobilia=talvez&condominio=&order=mais_relevantes"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

cards = soup.find_all("li", class_="Imoveis_cardDisplay__e0Dc8")

properties = []
titles = []
links = []
rooms = []
bathrooms = []
sizes = []
locations = []
rent = []
condominiums = []
phones = []

for card in cards:
    link = card.find("a")
    links.append("https://www.auroraimobi.com.br" + link["href"])


def get_details_page(aparment_url):
    details_page = requests.get(aparment_url)
    soup = BeautifulSoup(details_page.content, "html.parser")

    title = soup.find("span", class_="mb-4").text

    aparment_details = soup.find_all("span", class_="Caracteristica_title__vzVJS")

    aparment_locations = soup.find_all("address", class_="mb-1", itemprop="address")

    aparment_phone = soup.find(
        "span", class_="ArboPhone_spaceBetweenNumberAndIcon__eC6kC"
    ).text

    for location in aparment_locations:
        locations.append(location.text.strip())

    aparment_prices = soup.find_all("span", class_="", itemprop="price")
    apartment_rent = int(aparment_prices[0].text.strip().split()[1].replace(".", ""))
    apartment_condominium = int(
        aparment_prices[1].text.strip().split()[1].replace(".", "")
    )

    results = []
    for characteristic in aparment_details:
        value = re.findall(r"\d+", characteristic.text)
        results.append(value[0] if value else None)

    rooms.append(results[0])
    bathrooms.append(results[1])
    sizes.append(results[2])
    rent.append(apartment_rent)
    condominiums.append(apartment_condominium)
    titles.append(title)
    phones.append(aparment_phone)


for link in links:
    details = get_details_page(link)

json_list = []
for i in range(len(titles)):
    obj = {}
    obj["titulo"] = titles[i]
    obj["localizacao"] = locations[i]
    obj["quartos"] = rooms[i]
    obj["banheiros"] = bathrooms[i]
    obj["tamanho"] = sizes[i]
    obj["aluguel"] = rent[i]
    obj["condominio"] = condominiums[i]
    obj["contato"] = phones[i]
    obj["link"] = links[i]
    json_list.append(obj)

filename = "sample.json"

mount_json(filename, json_list)
