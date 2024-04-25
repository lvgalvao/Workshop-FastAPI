from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
import joblib  # Modificado aqui

app = FastAPI()

# Carregando o modelo previamente treinado
modelo = joblib.load("modelo_casas.pkl")

class DadosCasa(BaseModel):
    tamanho: PositiveFloat
    quartos: PositiveInt
    n_vagas: PositiveInt

class PrecoCasaRequest(DadosCasa):
    # Herda tamanho, quartos e n_vagas automaticamente
    email: Optional[EmailStr] = None

class PrecoCasaResponse(BaseModel):
    preco_estimado: PositiveFloat
    dados: PrecoCasaRequest

CRM = []

@app.post("/prever/", response_model=PrecoCasaResponse)
def prever_preco(preco_request: PrecoCasaRequest):
    # Preparando os dados para o modelo
    dados_entrada = [[preco_request.tamanho, preco_request.quartos, preco_request.n_vagas]]
    
    try:
        preco_estimado = modelo.predict(dados_entrada)[0]
        resposta = PrecoCasaResponse(preco_estimado=preco_estimado, dados=preco_request)
        CRM.append(preco_request.model_dump())
        print(CRM)
        return resposta
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))