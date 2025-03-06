# File: FS/Dockerfile

FROM python:3.9

WORKDIR /app

COPY fibonacci_server.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "fibonacci_server.py"]

