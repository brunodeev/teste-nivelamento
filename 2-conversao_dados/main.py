import pdfplumber
import pandas as pd
import requests

pdf_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
pdf_file = "anexo_i.pdf"

with open(pdf_file, "wb") as f:
    f.write(requests.get(pdf_url).content)

dados = []
with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table and all(len(row) == len(table[0]) for row in table):
                dados.extend(table)

df = pd.DataFrame(dados)

df = df[df[df.columns[0]] != df.columns[0]]

df.replace({
    "OD": "Consultas e outros procedimentos realizados por cirurgiões-dentistas",
    "AMB": "Procedimentos realizados em ambiente ambulatorial"
}, inplace=True)

csv_file = "rol_procedimentos.csv"
df.to_csv(csv_file, index=False, encoding="utf-8-sig")