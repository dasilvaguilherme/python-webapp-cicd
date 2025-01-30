import logging
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel


class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.args and len(record.args) >= 3 and record.args[2] != "/health"

logging.getLogger("uvicorn.access").addFilter(EndpointFilter())

class HealthResponse(BaseModel):
    status: str = "OK"

class GenerateRequest(BaseModel):
    input: dict  

app = FastAPI(title="Simple Web Application")

@app.get("/")
def index():
    return RedirectResponse("/docs")

@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Returns HTTP status 200 OK",
    status_code=status.HTTP_200_OK,
    response_model=HealthResponse)
def get_health():
    return HealthResponse(status="OK")

@app.post(
    "/generate",
    summary="Generate a response",
    response_description="Returns HTTP status 200 OK",
    status_code=status.HTTP_200_OK,
    response_model=dict)
def generate_response(request: GenerateRequest):

    input_data = request.input  

    return {"message": "Generation request received.", "input": input_data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
