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

        return json.dumps(aps, ensure_ascii=False)


    def get_infos(self, link):
        aux = {}
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        aux['titulo'] = soup.find("title").text.splitlines()[0]
        aux["localizacao"] = '';
        aux["quartos"] = '';
        aux["banheiros"] = '';
        aux["tamanho"] = '';
        aux["aluguel"] = '';
        aux["condominio"] = '';
        aux["contato"] = '';
        aux["link"] = '';

        return aux


newsletter = Dudu(
    "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",
    "https://www.santamerica.com.br/alugar/apartamento-para-alugar/pr/londrina"
)
print(newsletter.get_notices())
