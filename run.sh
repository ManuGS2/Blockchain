pip install -r requirements.txt
export FLASK_APP=blockchain_server/blockchain_api.py
nohup python run_app.py &
flask run --port 8000
