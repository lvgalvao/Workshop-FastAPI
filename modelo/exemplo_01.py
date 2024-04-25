from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import Body

import joblib  # Modificado aqui

app = FastAPI()

# Decorator
@app.get("/")
# Function é função padrão do Python
def root(): # O nome não importa
    return {"message": "Bem vindo a Jornada"} # Essa será a data que vamos retornar ao usuário

# Carregando o modelo previamente treinado
modelo = joblib.load("modelo_casas.pkl")

# class Casa(BaseModel):
#     tamanho: float
#     quartos: int

@app.post("/prever/")
def prever_preco(tamanho: float = Body(...), quartos: int = Body(...)):
    # Preparando os dados para o modelo
    print(tamanho)
    print(quartos)
    dados_entrada = [[tamanho, quartos]]
    
    try:
        # Fazendo a previsão usando o modelo
        preco_estimado = modelo.predict(dados_entrada)
        return {"preco_estimado": preco_estimado[0]}
    except Exception as e:
        # Tratamento de exceção para qualquer erro durante a previsão
        raise HTTPException(status_code=500, detail=str(e))
