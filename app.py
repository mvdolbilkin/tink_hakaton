from flask import Flask, request, redirect, url_for, render_template
from budgetcalculation import budget_calculation  # Импортируем метод из другого файла

app = Flask(__name__)

# Главная страница с формой
@app.route('/')
def index():
    return render_template('index.html')

# Обработчик POST-запроса от формы
@app.route('/budget-calculation', methods=['POST'])
def submit_id():
    brand_id = request.form.get('brand_id')
    if brand_id:
        # Перенаправляем на страницу /budgetcalculation/<id>
        return redirect(url_for('budget_calculation_route', user_id=brand_id))
    return "Error: ID is missing"

# Страница с расчетом бюджета, использующая функцию из другого файла
@app.route('/budget-calculation/<user_id>', methods=['GET'])
def budget_calculation_route(user_id):
    # Вызываем функцию из budgetcalculation.py и передаем результат в шаблон
    result = budget_calculation(user_id)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
