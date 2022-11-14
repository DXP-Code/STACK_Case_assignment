import csv

with open("Начисления_абоненты.csv", encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ";")

    res = {}

    # Группировка по домам и сортировка от 1 до ... дома
    for line in file_reader:
        sum = float(line['Начислено'])
        home = line['№ дома']
        street = line['Улица']
        try:
            res[(street),home] += sum
        except KeyError:
            res[(street),home] = sum

    res = sorted(res.items(), key=lambda item: item[0], reverse=False)

count = 0
i = 0

if count == 0:
    f = open('Начисления_дома.csv', mode="w", encoding='utf-8')
    file_writer = csv.writer(f, delimiter=";", lineterminator="\r")
    file_writer.writerow(["№ строки", "Улица", "№ дома", "Начислено по дому"])

# Запись в файл
for row in res:
    count += 1 # Обнавляет номер строки
    file_writer.writerow([count, row[0][0], row[0][1], res[i][1]])
    i += 1
