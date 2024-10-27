import csv
import os

# Определяем путь к файлу относительно текущего файла
file_path = os.path.join('..', 'data', 'brand_agg_statistic.csv')

def get_data(brand_id, file_path):

    # Считываем всех пользователей из файла с клиентами
    with open(file_path, encoding="utf8") as f:
        input_users = list(csv.DictReader(f))  # Преобразуем в список для многократного использования
    all_trxn_sum = 0
    all_trxn_count = 0
    # Проходим по нескольким файлам с транзакциями
    for i in range(1, 2):
        transactions_path = f"C:/Users/92552/PycharmProjects/tinkdatanalyze/data/transactions_1_2.csv"

        with open(transactions_path, encoding="utf8") as f:
            transactions_data = list(csv.DictReader(f))  # Считываем данные как список
            # Ищем совпадения клиентов из input_users в transactions_data
            for user_row in input_users:
                for transactions_row in transactions_data:
                    if (transactions_row["client_id"] == user_row["client_id"] and transactions_row["brand_id"] == brand_id):
                        # Суммируем значение trxn_sum, заменяя запятые на точки
                        all_trxn_sum += float(transactions_row["trxn_sum"].replace(",", "."))
                        all_trxn_count += 1
                        print(f"Совпадение: {user_row['client_id']} -> Сумма транзакций: {all_trxn_sum} Колво{all_trxn_count}")

    print(f"GMV (Gross Merchandise Value) - общую сумму, которую потратят клиенты: {all_trxn_sum / all_trxn_count}")
    return all_trxn_sum / all_trxn_count

def budget_calculation(brand_id, file_path):
    # Логика расчета бюджета для данного user_id
    # Например, возвращаем строку с расчетами
    return f"Budget Calculation for ID: {get_data(brand_id, file_path)} with calculated values."
