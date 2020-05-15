FROM python:3.7-slim
WORKDIR /server
COPY . .
ENV FLASK_APP blockchain_api.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask", "run", "--port", "8000"]