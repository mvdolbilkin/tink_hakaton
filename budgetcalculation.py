import csv
import os

# Определяем путь к файлу относительно текущего файла
file_path = os.path.join('..', 'data', 'brand_agg_statistic.csv')

def get_data(brand_id):
    with open('C:/Users/92552/PycharmProjects/tink_hakaton/data/brand_agg_statistic.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        trxn_sum = []
        for row in reader:
            if brand_id == row['brand_id']:
                trxn_sum.append(float(row["trxn_sum"]))
    return sum(trxn_sum) / len(trxn_sum)

def budget_calculation(brand_id):
    # Логика расчета бюджета для данного user_id
    # Например, возвращаем строку с расчетами
    return f"Budget Calculation for ID: {get_data(brand_id)} with calculated values."
