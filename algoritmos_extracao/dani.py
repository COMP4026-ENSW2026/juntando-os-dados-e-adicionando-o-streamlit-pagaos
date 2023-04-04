import requests
from bs4 import BeautifulSoup
import openai
import smtplib

# Key api GPT-3
openai.api_key = "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"


# Requests para pegar as ofertas no site da Veneza
URL = 'https://www.veneza.com.br/imoveis/apartamento-alugar-londrina'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#links = soup.find_all("div", class_="jetgrid__col--6 jetgrid__col--md-8 jetgrid__col--sm-12 jetgrid__col--xs-24")
#links = soup.find_all("div", class_="list__hover")
url = soup.find_all("a", class_="list__link")
base_url = "https://www.veneza.com.br"

for link in url:
    full_url = str(base_url) + str(link['href'])
    print("\n")
    print(full_url)
  
    def information(link):
        page = requests.get(full_url)
        soup = BeautifulSoup(page.content, "html.parser")
        teste = soup.find_all("div", class_="container")

        for div in teste:
            titulo = div.find("h1", class_="card__type")
            codigo_anuncio = div.find("p", class_="card__reference")
            localizacao = div.find("p", class_="card__address")
            quartos = div.find("div", class_="card__element jetgrid jetgrid--justify-left jetgrid--align-center")
            tamanho = div.find("div", class_="jetgrid jetgrid--align-center")
            valor_aluguel = div.find("p", class_="ui__text--green")
            valor_condominio = div.find("p", class_="ui__text--blue")
            descricao = div.find("p", class_="card__text")

            try:
                print(titulo.text.strip())
                print(codigo_anuncio.text.strip())
                print(localizacao.text.split())
                print(quartos.text.split())
                print(tamanho.text.strip())
                print(valor_aluguel.text.strip())
                print(valor_condominio.text.strip())
                print(descricao.text.strip())

            except:
                print("none")


    information(link)
