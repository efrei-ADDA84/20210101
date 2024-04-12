FROM python:3.9-slim

WORKDIR /app

COPY meteo.py .

RUN pip install --no-cache-dir requests Flask

CMD ["python", "meteo.py"]
