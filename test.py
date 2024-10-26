from flask import Flask
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, world!"

@app.route('/budget-calculation', methods=['POST'])
def post_budgetCalculation():
    return f"post_budgetCalculation"


@app.route('/budget-calculation/<id>', methods=['GET'])
def get_budgetCalculation(id):
    return f"get_budgetCalculation {id}"




# Обертка WSGI в ASGI
asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=80)
