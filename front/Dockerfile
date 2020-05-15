FROM python:3.7-slim
EXPOSE 5000
WORKDIR /front
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "run_app.py"]