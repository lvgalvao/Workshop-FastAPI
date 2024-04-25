FastAPI Simple content negotiation

https://medium.com/@denniskoko/implementing-content-negotiation-in-fastapi-371d03c59c02

https://medium.com/@denniskoko/content-negotiation-the-art-and-science-of-giving-clients-of-your-api-the-data-they-want-in-the-aa58e4eb1661

https://fastapi.tiangolo.com/tutorial/response-model/


# Multiple response

Para chamar os exemplos da API FastAPI que você forneceu usando `curl`, você precisará fazer duas chamadas distintas: uma que utilize o parâmetro `teleport` como `false` para obter uma resposta JSON simples e outra onde `teleport` seja `true`, resultando em um redirecionamento. Aqui estão os comandos `curl` para ambos os casos:

### 1. Chamada `curl` para JSONResponse

Este comando faz uma requisição para a rota `/portal` sem ativar o redirecionamento, esperando receber uma resposta JSON com uma mensagem.

```bash
curl -X GET 'http://127.0.0.1:8000/portal'
```

Ou, explicitamente passando `teleport=false`:

```bash
curl -X GET 'http://127.0.0.1:8000/portal?teleport=false'
```

### Resposta Esperada

Se o servidor estiver rodando e configurado corretamente, a resposta será:

```json
{
  "message": "Here's your interdimensional portal."
}
```

### 2. Chamada `curl` com Redirecionamento

Este comando faz uma requisição para a rota `/portal` com o parâmetro `teleport` configurado como `true`, o que acionará um redirecionamento para a URL especificada.

```bash
curl -L -X GET 'http://127.0.0.1:8000/portal?teleport=true'
```

A opção `-L` instrui o `curl` a seguir redirecionamentos. O servidor irá responder com um redirecionamento `302 Found` para a URL especificada, e o `curl` seguirá para essa nova localização, que é uma página no YouTube.

### Resposta Esperada

Como o redirecionamento aponta para o YouTube, você será levado à página do vídeo correspondente ao link fornecido. Se não usar o `-L`, o `curl` apenas mostrará os detalhes do cabeçalho de resposta indicando o redirecionamento:

```python-repl
HTTP/1.1 307 Temporary Redirect
location: https://www.youtube.com/watch?v=dQw4w9WgXcQ
...
```

### Considerações

* Certifique-se de que seu servidor FastAPI esteja rodando localmente e acessível no endereço `http://127.0.0.1:8000`.
* A utilização da flag `-L` no `curl` é essencial para seguir o redirecionamento, como demonstrado no segundo comando.
* Esses comandos são básicos e supõem que não há autenticação ou outras complicações na API que exigiriam cabeçalhos adicionais ou configurações.

Estes comandos `curl` permitem testar as duas funcionalidades implementadas na rota `/portal` de seu aplicativo FastAPI, demonstrando tanto a resposta direta quanto o comportamento de redirecionamento baseado no parâmetro fornecido.