import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# URL da API
url = "https://api.openai.com/v1/images/generations"


# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"  # Substitua $OPENAI_API_KEY pelo seu token real
}

n_quartos = 2
n_banheiros = 2
area_total = 150

prompt = f"""
        Generate a blueprint for a functional {n_quartos} bedroom apartment spanning {area_total} 
        square meters. The layout should have {n_banheiros} bathrooms and clearly defined rooms and 
        corridors, with precise measurements labeled for each. Please also incorporate 
        key elements such as windows and doors. Furthermore, if possible, include a proposed 
        furniture layout to offer a complete and comprehensive view of the living space.
        """

# Dados a serem enviados como corpo da requisição
body = {
    "model": "dall-e-3",
    "prompt": prompt,
    "n": 1,
    "size": "1024x1024"
}

# Realizando a requisição POST
response = requests.post(
    url, 
    headers=headers, 
    data=json.dumps(body))

print(response.status_code)
print(response.json())

URL_IMAGE = response.json()["data"][0]["url"]

imagem_path = "download_image.jpg"

print(requests.get(URL_IMAGE).content)

with open(imagem_path, "wb") as file:
    file.write(requests.get(URL_IMAGE).content)
