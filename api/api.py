from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

try:
    df_operadoras = pd.read_csv("api/Relatorio_cadop.csv", sep=";", encoding="utf-8-sig")
except UnicodeDecodeError:
    df_operadoras = pd.read_csv("api/Relatorio_cadop.csv", sep=";", encoding="latin1")

df_operadoras["Data_Registro_ANS"] = pd.to_datetime(df_operadoras["Data_Registro_ANS"], errors="coerce")

@app.get("/operadoras-relevantes")
def operadoras_relevantes():
    df_filtrado = df_operadoras[
        df_operadoras["Nome_Fantasia"].notna() &
        df_operadoras["Telefone"].notna() &
        df_operadoras["Endereco_eletronico"].notna()
    ]

    df_ordenado = df_filtrado.sort_values(by="Data_Registro_ANS", ascending=False)

    top10 = df_ordenado.head(10)

    colunas = [
        "Registro_ANS", "Razao_Social", "Nome_Fantasia", "Modalidade",
        "Cidade", "UF", "Telefone", "Endereco_eletronico", "Data_Registro_ANS"
    ]

    top10["Data_Registro_ANS"] = top10["Data_Registro_ANS"].dt.strftime("%Y-%m-%d")
    resultados = top10[colunas].to_dict(orient="records")
    return JSONResponse(content={"mais_relevantes": resultados})