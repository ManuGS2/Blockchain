FROM python:3.7-slim
ARG PORT
ARG HOST

ENV FLASK_APP run_app.py
ENV command "flask run --port $PORT"
ENV FLASK_RUN_HOST ${HOST}

COPY run_app.py .
COPY requirements.txt .
WORKDIR /front
COPY . .
WORKDIR ..

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ${command}