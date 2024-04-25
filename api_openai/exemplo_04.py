from abc import ABC, abstractmethod
import requests
import json
from dotenv import load_dotenv
import os
from typing import Optional

class APIGenericCollector(ABC):
    """ Classe abstrata para coletar dados de uma API. """

    def __init__(self, url: str , headers: dict, body=Optional[dict]):
        self.url = url
        self.headers = headers
        self.body = body

    @abstractmethod
    def make_request(self):
        """ Método para fazer a requisição à API. """
        pass

    @abstractmethod
    def parse_response(self, response=None):
        """ Método para analisar a resposta da API. """
        pass

class APICasaGenerator(APIGenericCollector):
    """ Classe específica para coletar imagens de uma API. """

    def __init__(self, prompt, n_quartos, area_total, n_banheiros):
        self.prompt = prompt
        self.n_quartos = n_quartos
        self.area_total = area_total
        self.n_banheiros = n_banheiros
        super().__init__(url, metodo, headers, body)

    def make_request(self):
        """ Faz uma requisição POST à API e retorna a resposta. """
        return requests.post(self.url, headers=self.headers, data=json.dumps(self.body))

    def parse_response(self, response):
        """ Analisa a resposta e retorna o conteúdo da imagem. """
        return requests.get(response.json()["data"][0]["url"]).content

    def generate_and_download_image(self):
        """ Executa o processo completo de geração e download da imagem. """
        response = self.make_request()
        image_content = self.parse_response(response)
        return image_content

# Exemplo de uso

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

collector = APICasaGenerator(
    url="https://api.openai.com/v1/images/generations",
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        },
    body = {
            "model": "dall-e-3",
            "prompt": prompt,
            "n": 1,
            "size": "1024x1024"
        }

    
)
image_content = collector.generate_and_download_image()
# Salvar a imagem em um arquivo, por exemplo:
with open('downloaded_image.png', 'wb') as file:
    file.write(image_content)
