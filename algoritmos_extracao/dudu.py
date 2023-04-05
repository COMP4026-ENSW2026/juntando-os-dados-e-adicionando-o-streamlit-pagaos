import requests
import openai
import smtplib
import json
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mount_json import mount_json


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

        return aps


    def get_infos(self, link):
        aux = {}
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        titulo = soup.find("title").text.splitlines()[0]
        quarto = int(
            soup
                .find_all("div", class_="col-xs-6")[0]
                .text
                .replace(' Dormitórios', '')
                .strip()
        )
        banheiro = int(
            soup
                .find_all("div", class_="col-xs-6")[1]
                .text
                .replace(' Banheiros', '')
                .strip()
        )
        tamanho = soup.find_all("div", class_="col-xs-6")[4].text.replace('m² imóvel', '').strip()
        aluguel = float(
            soup
                .find("h2", class_="elementor-heading-title")
                .text
                .replace('R$ ', '')
                .replace('.', '')
                .replace(',', '.')
        )
        condominio = soup.find_all("div", class_="elementor-clearfix")[2]
        condominio = float(
            condominio
                .find("p")
                .text
                .replace('*', '')
                .replace('*', '')
                .replace('Condomínio: R$ ', '')
                .replace('.', '')
                .replace(',', '.')
        )
        contato = soup.find("a", class_="btn-whatsapp-corretor")
        contato_formatado = ''
        if contato != None:
            contato_formatado = contato.text.strip()

        aux["titulo"] = titulo
        aux["localizacao"] = titulo.split('alugar no ')[-1]
        aux["quartos"] = quarto
        aux["banheiros"] = banheiro
        aux["tamanho"] = tamanho
        aux["aluguel"] = aluguel
        aux["condominio"] = condominio
        aux["contato"] = contato_formatado
        aux["link"] = link

        return aux


newsletter = Dudu(
    "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",
    "https://www.santamerica.com.br/alugar/apartamento-para-alugar/pr/londrina"
)

mount_json("imoveis.json", newsletter.get_notices())
