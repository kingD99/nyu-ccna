FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY authoritative_server.py .

CMD ["python", "authoritative_server.py"]
