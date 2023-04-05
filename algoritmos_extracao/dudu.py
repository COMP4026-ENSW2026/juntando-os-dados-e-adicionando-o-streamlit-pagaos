import requests
import openai
import smtplib
import json
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Dudu:
    def __init__(self, api_key, url):
        openai.api_key = api_key
        self.url = url
        self.page = requests.get(url)


    def get_notices(self):
        soup = BeautifulSoup(self.page.content, "html.parser")
        links = soup.find_all("a", class_="btn-info")
        aps = []

        for link in links:
            aps.append(self.get_infos(link['href']))

        return json.dumps(aps, indent=4, ensure_ascii=False)


    def get_infos(self, link):
        aux = {}
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        titulo = soup.find("title").text.splitlines()[0]
        aluguel = float(
            soup
                .find("h2", class_="elementor-heading-title")
                .text
                .replace('R$ ', '')
                .replace('.', '')
                .replace(',', '.')
        )
        contato = soup.find("a", class_="btn-whatsapp-corretor")
        contato_formatado = ''
        if contato != None:
            contato_formatado = contato.text.strip()

        aux["titulo"] = titulo
        aux["localizacao"] = titulo.split('alugar no ')[-1]
        aux["quartos"] = ''
        aux["banheiros"] = ''
        aux["tamanho"] = ''
        aux["aluguel"] = aluguel
        aux["condominio"] = ''
        aux["contato"] = contato_formatado
        aux["link"] = link

        return aux


newsletter = Dudu(
    "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",
    "https://www.santamerica.com.br/alugar/apartamento-para-alugar/pr/londrina"
)

with open("./sample.json", "w") as outfile:
    outfile.write(newsletter.get_notices())
