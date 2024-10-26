from flask import Flask
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, world!"

print(0)


# Обертка WSGI в ASGI
asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=80)
