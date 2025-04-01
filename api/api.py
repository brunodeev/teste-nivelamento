from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

df_operadoras = pd.read_csv("api/Relatorio_cadop.csv", sep=";", encoding="latin1")

df_operadoras["Data_Registro_ANS"] = pd.to_datetime(df_operadoras["Data_Registro_ANS"], errors="coerce")

@app.get("/operadoras")
def operadoras():
    return JSONResponse(content={operadoras})