## Objetivo

Este workshop visa introduzir os conceitos básicos e as práticas necessárias para criar uma API usando a framework FastAPI em Python. Os participantes aprenderão desde a configuração do ambiente de desenvolvimento até a criação e documentação de APIs simples.

## Programação

### 1. Introdução a APIs e Web Servers

* **O que é uma API?**
    * Explicação de API (Interface de Programação de Aplicações) como um conjunto de regras e especificações que softwares podem seguir para se comunicar.
* **Diferenças entre API e Web Server**
    * Clarificação de que um Web Server lida com requisições HTTP para servir conteúdo web, enquanto uma API fornece uma interface para realizar operações específicas através de um servidor.

### 2. Introdução ao FastAPI

* **Visão Geral do FastAPI**
    * Discussão sobre as características do FastAPI, como alta performance, fácil aprendizado e recursos como a geração automática de documentação.
* **Comparação com Outras Frameworks**
    * Breve comparação do FastAPI com outras frameworks populares como Flask e Django, destacando a facilidade de uso e eficiência em operações assíncronas.

### 3. Configuração do Ambiente de Desenvolvimento

* **Instalação do Python e Setup do Ambiente**
    * Passo a passo para configurar o ambiente Python, incluindo a instalação do FastAPI e do servidor Uvicorn usando pip.

### 4. Criando sua Primeira API com FastAPI

* **Hello World API**
    * Tutorial para criar um endpoint básico que retorna uma mensagem de "Hello, World!" usando FastAPI.

```python
from fastapi import FastAPI

app = FastAPI()

# Decorator -> É aqui que faz a mágica de transformar nossa função.
@app.get("/")
# Function é função padrão do Python
def root(): # O nome não importa
    return {"message": "Hello world!"} # Essa será a data que vamos retornar ao usuário
```

```bash
uvicorn main:app
```

```bash
uvicorn main:app --reload
```

HTTP metodos

#### Curl

Para usar `curl` para fazer uma requisição à sua API que está rodando com FastAPI, você pode enviar dados como JSON através de uma requisição POST. Suponhamos que você tenha um endpoint em sua API que espera receber os dados de uma casa e então retorna uma previsão de preço baseada nessas informações. Aqui está como você pode fazer isso com `curl`.

### Exemplo de Requisição com Curl

Suponha que seu endpoint para prever o preço da casa esteja configurado como `http://127.0.0.1:8000/prever/` e aceite um JSON com dois campos: `tamanho` e `quartos`. Aqui está como você pode enviar uma requisição:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/prever/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "tamanho": 120,
  "quartos": 3
}'
```

### Explicação do Comando Curl

* `-X 'POST'`: Especifica o método HTTP para a requisição, que é POST neste caso.
* `http://127.0.0.1:8000/prever/`: URL do endpoint da API.
* `-H 'accept: application/json'`: Define o cabeçalho HTTP para indicar que a resposta esperada deve ser em JSON.
* `-H 'Content-Type: application/json'`: Define o cabeçalho HTTP para indicar que o corpo da requisição está em formato JSON.
* `-d '{...}'`: Os dados sendo enviados à API. Substitua os valores de `tamanho` e `quartos` conforme necessário para os dados específicos da casa que você quer avaliar.

### Testando a Requisição

1. Certifique-se de que sua API FastAPI esteja rodando e acessível em `http://127.0.0.1:8000`.
2. Abra um terminal e execute o comando `curl` fornecido.
3. Observe a resposta da API, que deve incluir a previsão do preço da casa baseada nos dados fornecidos.

Usar os cabeçalhos Accept e Content-Type nas suas requisições HTTP é uma forma de comunicar claramente ao servidor tanto o formato dos dados que você está enviando quanto o formato que você espera receber em resposta:

Content-Type: application/json: Este cabeçalho informa ao servidor que o corpo da requisição que você está enviando está em formato JSON. É uma maneira de dizer, "Ei, os dados que estou enviando estão em JSON; por favor, interprete-os dessa forma."
Accept: application/json: Este cabeçalho diz ao servidor que você deseja que a resposta seja em JSON. Isso é particularmente útil em APIs que podem retornar dados em diferentes formatos. Ao especificar application/json, você está solicitando que a API responda com dados nesse formato específico.

#### Postman

Também temos a opção usar o Postman (uma aplicação)


### 5. Trabalhando com Dados

* **Uso de Modelos Pydantic**
    * Introdução aos modelos Pydantic para validação de dados e como integrá-los com FastAPI.
* **Endpoints GET e POST**
    * Criação de exemplos práticos de endpoints que lidam com métodos GET e POST para enviar e receber dados.

### 6. Uvicorn: O Servidor ASGI

* **Por que Uvicorn?**
    * Explicação sobre o papel do Uvicorn como um servidor ASGI, necessário para executar aplicações FastAPI de forma eficiente e assíncrona.

### 7. Documentação Automática

* **Swagger UI**
    * Demonstração de como acessar e utilizar a documentação automática gerada pelo FastAPI.

### 8. Exercícios Práticos

* **Hands-on Coding**
    * Série de exercícios práticos para aplicar o conhecimento adquirido na criação de APIs mais complexas.
* **Desafio com Banco de Dados**
    * Desafio para criar uma API que interage com um banco de dados usando operações básicas de CRUD.

### 9. Sessão de Perguntas e Respostas (Q&A)

* **Discussão Aberta**
    * Espaço para perguntas, troca de ideias e esclarecimento de dúvidas.

### 10. Encerramento

* **Recursos para Aprendizado Contínuo**
    * Compartilhamento de recursos adicionais, como documentação online, tutoriais e fóruns para aprofundamento nos temas abordados.

## Materiais Necessários

* Slides das apresentações.
* Códigos de exemplo e templates para exercícios.
* Acesso à Internet para documentação e pesquisa.

## Pré-requisitos

* Conhecimento básico de programação em Python.
* Ambiente de desenvolvimento Python configurado com acesso à internet.

## Recursos Adicionais

* Documentação Oficial do FastAPI
* Pydantic Documentation
* [Uvicorn Documentation](https://www.uvicorn.org/)


## Ideias

Async
Paginação
Autenticação