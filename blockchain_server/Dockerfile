FROM python:3.7-slim
EXPOSE 8000
WORKDIR /blockchain_server
COPY . .

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt --upgrade --no-cache

CMD ["sh" "run_app.sh"]