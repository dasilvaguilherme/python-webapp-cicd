FROM python:3.13.0-slim-bookworm

EXPOSE 8080/tcp

WORKDIR /app
COPY ./requirements.txt *.py  index.html ./
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["fastapi", "run", "/app/main.py", "--host", "0.0.0.0", "--port", "8080"]