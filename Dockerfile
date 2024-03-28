FROM python:3.9-slim

WORKDIR /app

COPY meteo.py .

RUN pip install requests

CMD ["python", "meteo.py"]
