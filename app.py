# app_b.py
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hola desde app B', 200

@app.route('/health', methods=['GET'])
def call_health():
    try:
        # Llamamos a la app B, que está en localhost:3001
        return 'OK', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500
@app.route('/startup', methods=['GET'])
def call_startup():
    try:
        # Llamamos a la app B, que está en localhost:3001
        return 'OK', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500
@app.route('/readiness', methods=['GET'])
def call_readiness():
    try:
        # Llamamos a la app B, que está en localhost:3001
        return 'OK', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)