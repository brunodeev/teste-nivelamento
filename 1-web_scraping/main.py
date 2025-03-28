import os
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

os.makedirs("downloads", exist_ok=True)
pdfs = []

for a in soup.find_all("a", href=True):
    text = a.text.strip()
    if text in ["Anexo I.", "Anexo II."]:
        print(text)