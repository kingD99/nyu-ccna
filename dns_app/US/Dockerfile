# File: US/Dockerfile

FROM python:3.9

WORKDIR /app

COPY user_server.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "user_server.py"]

