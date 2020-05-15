FROM python:3.7-slim
EXPOSE 5000
WORKDIR /blockchain_front
COPY . .


RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt --upgrade --no-cache

CMD ["python", "run_app.py"]