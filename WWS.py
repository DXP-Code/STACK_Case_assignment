# ______Working With Subscribers______
import csv
from dataclasses import dataclass


class Subscriber:
    def __init__(self,  type_of_accrual, previous_accruals, current_accruals):
        self.type_of_accrual = type_of_accrual
        self.previous_accruals = previous_accruals
        self.current_accruals = current_accruals


    def get_accruals(self):
        if self.type_of_accrual == 1:
            return 301.26
        else:
            return (self.current_accruals - self.previous_accruals) * 1.52

with open("абоненты.csv", encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter = ";")
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            f = open('Начисления_абоненты.csv', mode="w", encoding='utf-8')
            file_writer = csv.writer(f, delimiter=";", lineterminator="\r")
            file_writer.writerow(["Индекс", "Фамилия", "Улица",  "№ дома", "№ Квартиры",
                                  "Тип начисления", "Предыдущее", "Текущее", "Начислено"])
        # Запись в файл
        accrual = Subscriber(int(row['Тип начисления']), int(row['Предыдущее']), int(row['Текущее']))
        file_writer.writerow([row['Индекс'], row['Фамилия'], row['Улица'], row['№ дома'], row['№ Квартиры'], row['Тип начисления'], row['Предыдущее'], row['Текущее'], accrual.get_accruals()])
        count += 1
    print(f'Всего в файле {count + 1} строк.')


