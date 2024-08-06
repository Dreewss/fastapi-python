# API de Produtos

Uma API RESTful desenvolvida com FastAPI para gerenciar produtos em um sistema.

O que é uma RESTful API?

São serviços que permitem a separação total do cliente do servidor. Eles simplificam e desacoplam vários componentes do servidor para que cada parte possa evoluir independentemente.

## Funcionalidades

- **Listar todos os produtos:** `GET /products`
- **Adicionar um novo produto:** `POST /products`
- **Atualizar um produto existente:** `PUT /products/{id}`
- **Remover um produto:** `DELETE /products/{id}`

## Tecnologias Utilizadas

- FastAPI
- JSON para armazenamento de dados
- Requests

## Documentação

Acesse a documentação interativa da API [aqui](https://fastapi.tiangolo.com/) 

## Instruções de Configuração

1. Clone o repositório:
    ```bash
    git clone https://github.com/Dreewss/fastapi-python.git
    cd fastapi-python
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o servidor:
    ```bash
    uvicorn main:app --reload
    ```

## Deploy

Veja a aplicação ao vivo [aqui](https://youtu.be/ZbsfuEhHl2c).

## Objetivo do Projeto

Fornecer uma API simples e eficaz para gerenciar um catálogo de produtos com uma interface de documentação interativa.

---

Sinta-se à vontade para contribuir ou fazer sugestões!
