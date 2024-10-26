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

def generate_json_data(brand_id, ):
    # Здесь вы можете генерировать данные в зависимости от brand_id
    data = {
        "brand_id": brand_id,
        "client_file":
        "message": "Данные успешно сгенерированы",
        "status": "success"
    }
    return data
# Обработчик POST-запроса от формы
@app.route('/budget-calculation', methods=['POST'])
def submit_id():
    print(request.json())
    brand_id = request.form.get('brand_id')
    uploaded_file = request.files.get('client_file')

    if not brand_id:
        flash("Error: ID is missing")
        return redirect(url_for('index'))

        # Проверка на наличие загруженного файла
    if uploaded_file and uploaded_file.filename != '':
        filename = uploaded_file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)

        # Передаем brand_id и путь к файлу в метод budget_calculation
        result = budget_calculation(brand_id, file_path)
        return result
    else:
        flash("Error: File is missing")
        return redirect(url_for('index'))

@app.route('/budget-calculation', methods=['POST'])
def submit_id():
    data = request.json  # Get the JSON payload

    brand_id = data.get('brand_id')
    uploaded_file = data.get('client_file')

    if not brand_id:
        return {"error": "Error: ID is missing"}, 400  # Return a JSON error response

    # Handle file upload differently since it's not part of the JSON payload
    if 'client_file' in request.files:
        uploaded_file = request.files['client_file']
        if uploaded_file and uploaded_file.filename != '':
            filename = uploaded_file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(file_path)

            # Передаем brand_id и путь к файлу в метод budget_calculation
            result = budget_calculation(brand_id, file_path)
            return {"result": result}, 200  # Return a JSON response
        else:
            return {"error": "Error: File is missing"}, 400  # Return a JSON error response

    return {"error": "Error: No file uploaded"}, 400  # General error response
# Страница с расчетом бюджета, использующая функцию из другого файла
@app.route('/budget-calculation/<calc_id>', methods=['GET'])
def budget_calculation_route(calc_id):
    # Вызываем функцию из budgetcalculation.py и передаем результат в шаблон
    result = budget_calculation(calc_id)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
