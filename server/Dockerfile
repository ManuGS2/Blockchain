FROM python:3.7-slim
ARG PORT
ARG HOST

ENV FLASK_APP blockchain_api.py
ENV command "flask run --port $PORT"
ENV FLASK_RUN_HOST ${HOST}

WORKDIR /server
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ${command}