FROM python:3.7-slim
ENV FLASK_APP run_app.py

COPY run_app.py .
COPY requirements.txt .
WORKDIR /front
COPY . .
WORKDIR ..

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD "flask run"