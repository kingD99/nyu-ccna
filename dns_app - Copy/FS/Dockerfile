#    Docker For FS

FROM python:3.9-slim

WORKDIR /app

COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9090 

CMD ["python", "fibonacci_server.py"]  
