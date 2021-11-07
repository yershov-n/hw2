# 1. Создать view-функцию, которая будет возвращать средний рост и средний вес (в см и кг соответственно) для студентов
# из файла hw.csv
#
#   get_avr_data() -> 127.0.0.1:5000/avr_data
#
# 2. Создать view-функцию, которая возвращает содержимое файла с установленными пакетами в текущем проекте
# (requirements.txt)
#
#   get_requirements() -> 127.0.0.1:5000/requirements
#
# 3. Создать view-функцию, которая возвращает список случайных студентов. Использовать библиотеку faker.
#
#   get_random_students() -> 127.0.0.1:5000/random_students

from flask import Flask
import csv
from utils import inch2cm, pound2kg, get_students_list
from formater import list2htmlBR, str2htmlBR

app = Flask(__name__)


@app.route('/avr_data')
def get_avr_data():
    dct = {}
    height = 0
    weight = 0
    with open('hw.csv') as r_file:
        fieldnames = ['index', 'height(inc)', 'weight(p)']
        reader = csv.DictReader(r_file, fieldnames=fieldnames)
        next(reader, None)
        for row in reader:
            dct.update({row['index']: [float(row['height(inc)']), float(row['weight(p)'])]})
    for key, value in dct.items():
        height += value[0]
        weight += value[1]
    return f'Average height is {inch2cm(height/len(dct))} сm, average weight is {pound2kg(weight/len(dct))} kg.'


@app.route('/requirements')
def get_requirements():
    with open('requirements.txt', 'r') as r_file:
        return str2htmlBR(f'{r_file.read()}')


@app.route('/random_students')
def get_random_students():
    return list2htmlBR(get_students_list())


app.run(debug=True)
