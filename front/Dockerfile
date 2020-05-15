FROM python:3.7-slim
COPY run_app.py .
COPY requirements.txt .
WORKDIR /front
COPY . .
WORKDIR ..

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "run_app.py"]