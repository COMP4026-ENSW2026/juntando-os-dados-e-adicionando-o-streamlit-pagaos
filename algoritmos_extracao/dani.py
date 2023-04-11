import requests
from bs4 import BeautifulSoup
from mount_json import mount_json


# Requests para pegar as ofertas no site da Veneza
URL = 'https://www.veneza.com.br/imoveis/apartamento-alugar-londrina'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
url = soup.find_all("a", class_="list__link")
base_url = "https://www.veneza.com.br"


  
def information(links):
    
    page = requests.get(links)
    soup = BeautifulSoup(page.content, "html.parser")
    teste = soup.find_all("div", class_="container")

        
    for div in teste:
        aux = {}
        titles = div.find("h1", class_="card__type")
        locations = div.find("p", class_="card__address")
        rooms = div.find("div", class_="card__element jetgrid jetgrid--justify-left jetgrid--align-center")
        sizes = div.find("div", class_="jetgrid jetgrid--align-center")
        rent = div.find("p", class_="ui__text--green")
        condominiums = div.find("p", class_="ui__text--blue")
        phones = ("43-3371-0001")

        aux["titulo"] = titles.text.strip()
        aux["localizacao"] = locations.text.strip().replace("  ", "").replace("\n", " ")
        aux["quartos"] = rooms.text.strip().replace(" ", "").replace("quartos", "")
        aux["banheiros"] = ''
        aux["tamanho"] = aux["tamanho"] = sizes.text.strip().replace(" ", "").replace("total", "").replace("\u00A0", "")
        aux["aluguel"] = rent.text.strip()
        aux["condominio"] = ''
        if condominiums != None:
            aux["condominio"] = condominiums.text.strip()
        aux["contato"] = phones
        aux["link"] = links
    return(aux)
        
json_list = []
for link in url:
    links = str(base_url) + str(link['href'])
    json_list.append(information(links))


mount_json("imoveis.json", json_list)
