import csv
import json
import os

# Определяем путь к файлу относительно текущего файла
file_path = os.path.join('..', 'data', 'brand_agg_statistic.csv')

def get_data(brand_id, data_time, file_path):
    with open('result/data.json', 'r', encoding='utf-8') as json_file:
        sl = json.load(json_file)
    sl = sl[brand_id]
    print(sl.keys())
    data_time = data_time.split("-")

    # Считываем всех пользователей из файла с клиентами
    with open(file_path, encoding="utf8") as f:
        input_users = list(csv.DictReader(f))  # Преобразуем в список для многократного использования
    all_trxn_sum = 0
    all_trxn_count = 0
    arr_years = []
    # Проходим по нескольким файлам с транзакциями
    for i in range(len(list(sl.keys()))):
        all_trxn_sum = 0
        all_trxn_count = 0
        data_time[0] = str(int(data_time[0]) - i)
        for user_row in input_users:
            if "-".join(data_time) in sl:
                if user_row["client_id"] in sl["-".join(data_time)]:
                    all_trxn_sum += sl["-".join(data_time)][user_row["client_id"]]
            else:
                break
        if all_trxn_sum != 0:
            print(all_trxn_sum, all_trxn_count)
            arr_years.append(all_trxn_sum)

    print(arr_years)
    # print(f"GMV (Gross Merchandise Value) - общую сумму, которую потратят клиенты: {all_trxn_sum / all_trxn_count}")
    return sum(arr_years) / len(arr_years)
print(get_data("zii1gFsQg", "2024-08-01", "data/test_offer_clients2.csv"))
def budget_calculation(brand_id, file_path):
    # Логика расчета бюджета для данного user_id
    # Например, возвращаем строку с расчетами
    return f"Budget Calculation for ID: {get_data(brand_id, file_path)} with calculated values."
