import requests, os, zipfile
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

base_dir = os.path.dirname(os.path.abspath(__file__))
downloads_folder = os.path.join(base_dir, "downloads")
os.makedirs(downloads_folder, exist_ok=True)
pdfs = []

for a in soup.find_all("a", href=True):
    text = a.text.strip()
    if text in ["Anexo I.", "Anexo II."]:
        link = a['href']
        file_name = text.replace(" ", "_").replace(".", "").lower() + ".pdf"
        file_path = os.path.join(downloads_folder, file_name)
        print(f"Baixando {file_name}")
        file = requests.get(link, headers=headers)
        with open(file_path, "wb") as f:
            f.write(file.content)
        pdfs.append(file_path)

zip_path = os.path.join(base_dir, "anexos.zip")
with zipfile.ZipFile(zip_path, "w") as zipf:
    for p in pdfs:
        zipf.write(p, os.path.basename(p))

os.remove(os.path.join(downloads_folder, "anexo_i.pdf"))
os.remove(os.path.join(downloads_folder, "anexo_ii.pdf"))
os.removedirs(downloads_folder)

print("Arquivo ZIP gerado com sucesso.")