FROM python:3.7-slim
ARG PORT
ENV FLASK_APP blockchain_api.py
ENV command "flask run --port $PORT"

WORKDIR /server
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ${command}