# Simple Web Application

Este é um projeto de uma aplicação web simples construída com FastAPI. A aplicação possui endpoints para verificar a saúde e gerar respostas baseadas em requisições JSON.

## Estrutura do Projeto

```
my-fastapi-app/
├── app.py             # Código principal da aplicação FastAPI
├── requirements.txt   # Dependências do projeto
└── Dockerfile         # Arquivo para construir a imagem Docker
```

### Descrição dos Arquivos

- **app.py**: Contém a lógica da aplicação, incluindo os endpoints.
- **requirements.txt**: Lista as dependências necessárias para rodar a aplicação.
- **Dockerfile**: Usado para criar uma imagem Docker da aplicação.

## Pré-requisitos

Antes de começar, você precisará ter o Python 3.7 ou superior instalado em sua máquina. Além disso, é recomendável utilizar um ambiente virtual para gerenciar as dependências do projeto.

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu_usuario/simple-web-application.git
   cd simple-web-application
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

## Executando a Aplicação

Para iniciar a aplicação, execute o seguinte comando:

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:80`.

## Endpoints

### 1. `/`

- **Método**: GET
- **Descrição**: Redireciona para a documentação da API.
- **Resposta**: Redireciona para `/docs`.

### 2. `/health`

- **Método**: GET
- **Descrição**: Realiza uma verificação de saúde da aplicação.
- **Resposta**:
  - Status Code: `200 OK`
  - Corpo:
    ```json
    {
      "status": "OK"
    }
    ```

### 3. `/generate`

- **Método**: POST
- **Descrição**: Recebe um JSON com a estrutura `{ "input": {} }` e retorna uma confirmação.
- **Requisição**:
  - Exemplo de corpo:
    ```json
    {
      "input": {}
    }
    ```
- **Resposta**:
  - Status Code: `200 OK`
  - Corpo:
    ```json
    {
      "message": "Generation request received.",
      "input": {}
    }
    ```

## Executando com Docker

Se preferir, você pode executar a aplicação utilizando Docker:

1. **Construa a imagem Docker**:
   ```bash
   docker build -t my-fastapi-app .
   ```

2. **Execute o contêiner**:
   ```bash
   docker run -p 80:80 my-fastapi-app
   ```

A aplicação estará disponível em `http://localhost`.
