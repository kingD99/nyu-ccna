FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fibonacci_server.py .

CMD ["python", "fibonacci_server.py"]
