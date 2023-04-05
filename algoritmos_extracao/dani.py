import requests
from bs4 import BeautifulSoup
import openai
import smtplib
from mount_json import mount_json

# Key api GPT-3
openai.api_key = "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"


# Requests para pegar as ofertas no site da Veneza
URL = 'https://www.veneza.com.br/imoveis/apartamento-alugar-londrina'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
url = soup.find_all("a", class_="list__link")
base_url = "https://www.veneza.com.br"

for link in url:
    links = str(base_url) + str(link['href'])
    print("\n")
    print(links)
  
    def information(link):
        page = requests.get(links)
        soup = BeautifulSoup(page.content, "html.parser")
        teste = soup.find_all("div", class_="container")

        for div in teste:
            titles = div.find("h1", class_="card__type")
            codigo_anuncio = div.find("p", class_="card__reference")
            locations = div.find("p", class_="card__address")
            rooms = div.find("div", class_="card__element jetgrid jetgrid--justify-left jetgrid--align-center")
            sizes = div.find("div", class_="jetgrid jetgrid--align-center")
            rent = div.find("p", class_="ui__text--green")
            condominiums = div.find("p", class_="ui__text--blue")
            descricao = div.find("p", class_="card__text")
            phones = ("43-3371-0001")

            try:
                print(titles.text.strip())
                print(codigo_anuncio.text.strip())
                print(locations.text.split())
                print(rooms.text.split())
                print(sizes.text.strip())
                print(rent.text.strip())
                print(condominiums.text.strip())
                print(descricao.text.strip())
                print(phones)

            except:
                print("none")


    information(link)

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