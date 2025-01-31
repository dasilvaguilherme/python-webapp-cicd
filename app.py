"""
Módulo principal para a API de geração de imagens.

Este módulo utiliza FastAPI para expor endpoints REST para geração e
retorno de imagens baseadas nos parâmetros fornecidos pelo usuário.
"""

import json
import asyncio
import base64
import logging
from io import BytesIO

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, FileResponse
from pydantic import BaseModel

import generator


with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

class HealthResponse(BaseModel):
    """Modelo de resposta para verificação de saúde do sistema."""
    status: str = "OK"


class GenerateImageRequest(BaseModel):
    """Modelo para a requisição de geração de imagem."""
    width: int = 640
    height: int = 480
    iterations: int = 100
    re_min: float = -2.0
    re_max: float = 1.0
    im_min: float = -1.0
    im_max: float = 1.0
    delay: int = 0


class GenerateImageResponse(BaseModel):
    """Modelo para a resposta da geração de imagem."""
    image: str


app = FastAPI(title="generator")


@app.get("/")
def index():
    """Redireciona para a interface do usuário."""
    return RedirectResponse("/ui")


@app.post("/generate", response_model=GenerateImageResponse)
async def generate_image(req: GenerateImageRequest):
    """Gera uma imagem com os parâmetros fornecidos."""
    if req.delay != 0:
        await asyncio.sleep(req.delay)

    img = generator.generate(
        req.width,
        req.height,
        req.iterations,
        req.re_min,
        req.re_max,
        req.im_min,
        req.im_max,
    )

    buffered = BytesIO()
    img.save(buffered, format="png")
    return GenerateImageResponse(image=base64.b64encode(buffered.getvalue()).decode("utf-8"))


@app.get("/health", response_model=HealthResponse)
def get_health():
    """Verifica a saúde do serviço."""
    return HealthResponse(status="OK")


@app.get("/ui", response_class=FileResponse)
def get_ui():
    """Serve o arquivo index.html."""
    return FileResponse("index.html")


class EndpointFilter(logging.Filter):  # pylint: disable=too-few-public-methods
    """Filtro para remover logs desnecessários do endpoint /health."""
    def filter(self, record: logging.LogRecord) -> bool:
        """Verifica se o log é referente ao endpoint /health e o filtra."""
        return record.args and len(record.args) >= 3 and record.args[2] != "/health"


logging.getLogger("uvicorn.access").addFilter(EndpointFilter())


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=config['server']['host'],
        port=config['server']['port'],
        log_level=config['logging']['level'].lower()
    )
    