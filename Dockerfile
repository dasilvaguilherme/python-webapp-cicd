FROM python:3.13.0-slim-bookworm

EXPOSE 8080/tcp

WORKDIR /app

COPY ./requirements.txt *.py  config.json index.html ./
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python3", "/app/app.py"]