from flask import Flask
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Главная страница с формой
@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Budget Calculation</title>
            </head>
            <body>
                <h1>Enter your ID for Budget Calculation</h1>
                <form action="/submit-id" method="POST">
                    <label for="user_id">Enter ID:</label>
                    <input type="text" id="user_id" name="user_id" required>
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>
    '''

# Обработчик POST-запроса от формы
@app.route('/submit-id', methods=['POST'])
def submit_id():
    user_id = request.form.get('user_id')
    if user_id:
        # Перенаправляем на страницу /budgetcalculation/<id>
        return redirect(url_for('budget_calculation', user_id=user_id))
    return "Error: ID is missing"

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
