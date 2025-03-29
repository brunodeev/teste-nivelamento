import tabula
import requests
import os

pdf_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
pdf_file = "anexo_i.pdf"

if not os.path.exists(pdf_file):
    r = requests.get(pdf_url)
    with open(pdf_file, "wb") as f:
        f.write(r.content)

tabula.environment_info()
dfs = tabula.read_pdf(pdf_file, encoding='latin1', pages="all", multiple_tables=True)

print(dfs)