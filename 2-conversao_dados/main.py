import zipfile
import requests
import pdfplumber
import pandas as pd
import os

pdf_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

base_dir = os.path.dirname(os.path.abspath(__file__))

pdf_path = os.path.join(base_dir, "anexo_i.pdf")
csv_path = os.path.join(base_dir, "rol_procedimentos.csv")
zip_path = os.path.join(base_dir, "Teste_Bruno.zip")

with open(pdf_path, "wb") as f:
    f.write(requests.get(pdf_url).content)

dados_extraidos = []

with pdfplumber.open(pdf_path) as pdf:
    for page_number in range(2, len(pdf.pages)):
        page = pdf.pages[page_number]
        tables = page.extract_tables()
        for table in tables:
            if all(len(row) == len(table[0]) for row in table):
                dados_extraidos.extend(table)

df = pd.DataFrame(dados_extraidos)

df = df[df[0] != "PROCEDIMENTO"]
df.dropna(how="all", inplace=True)

df.replace({
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}, inplace=True)

df.to_csv(csv_path, index=False, encoding="utf-8-sig")

with zipfile.ZipFile(zip_path, "w") as zipf:
    zipf.write(csv_path, arcname="rol_procedimentos.csv")

os.remove(pdf_path)
os.remove(csv_path)

print("Processamento finalizado.")