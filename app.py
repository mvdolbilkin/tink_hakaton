from flask import Flask, request, redirect, url_for, render_template, flash
from budgetcalculation import budget_calculation  # Импортируем метод из другого файла
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# Главная страница с формой
@app.route('/')
def index():
    return render_template('index.html')

# Обработчик POST-запроса от формы
@app.route('/budget-calculation', methods=['POST'])
def submit_id():
    brand_id = request.form.get('brand_id')
    uploaded_file = request.files.get('client_file')
    #uploaded_link = request.form.get('file_link')

    if uploaded_file and uploaded_file.filename != '':
        filename = uploaded_file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)
        result = budget_calculation(brand_id, file_path)
        return result

    # if uploaded_link != "":
    #     filename = какая то функци для s3
    #     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    #     uploaded_link.save(file_path)




@app.route('/budget-calculation/<calc_id>', methods=['GET'])
def budget_calculation_route(calc_id):
    # Вызываем функцию из budgetcalculation.py и передаем результат в шаблон
    result = budget_calculation(calc_id)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
