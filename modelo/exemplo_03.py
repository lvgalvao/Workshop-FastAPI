from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib  # Modificado aqui

app = FastAPI()

# Decorator
@app.get("/")
# Function é função padrão do Python
def root(): # O nome não importa
    return {"message": "Bem vindo a Jornada"} # Essa será a data que vamos retornar ao usuário

# Carregando o modelo previamente treinado
modelo = joblib.load("modelo_casas.pkl")

class DadosCasa(BaseModel):
    tamanho: int
    quartos: int

class CasaRequest(DadosCasa):
    pass

class PrecoCasaResponse(BaseModel):
    preco_estimado: float
    dados: DadosCasa

previsoes = []

@app.post("/prever/")
def prever_preco(casa: CasaRequest):
    # Preparando os dados para o modelo
    dados_entrada = [[casa.tamanho, casa.quartos]]
    
    try:
        # Fazendo a previsão usando o modelo
        preco_estimado = modelo.predict(dados_entrada)
        return PrecoCasaResponse(preco_estimado= preco_estimado[0], dados= casa)
    except Exception as e:
        # Tratamento de exceção para qualquer erro durante a previsão
        raise HTTPException(status_code=500, detail=str(e))
