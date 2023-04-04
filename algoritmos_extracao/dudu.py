import requests
import openai
import smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Newsletter:
    def __init__(self, api_key, url):
        openai.api_key = api_key
        self.url = url
        self.page = requests.get(url)


    def get_notices(self):
        soup = BeautifulSoup(self.page.content, "html.parser")
        links = soup.find_all("a", class_="btn-info")

        for link in links:
            self.get_infos(link['href'])


    def get_infos(self, link):
        page = requests.get(link)
        soup = BeautifulSoup(self.page.content, "html.parser")
        links = soup.find_all("a", class_="btn-info")
        print(page)

newsletter = Newsletter(
    "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",
    "https://www.santamerica.com.br/alugar/apartamento-para-alugar/pr/londrina"
)
newsletter = Newsletter(
    "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",
    "https://www.santamerica.com.br/alugar/apartamento-para-alugar/pr/londrina"
)
newsletter = Newsletter(
    "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",
    "https://www.santamerica.com.br/alugar/apartamento-para-alugar/pr/londrina"
)
newsletter = Newsletter(
    "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",
    "https://www.santamerica.com.br/alugar/apartamento-para-alugar/pr/londrina"
)
newsletter = Newsletter(
    "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",
    "https://www.santamerica.com.br/alugar/apartamento-para-alugar/pr/londrina"
)
newsletter.get_notices()
