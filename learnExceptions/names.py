import random

names = ['Руслан', 'Сергей', 'Колян', 'Рома', 'Дима', 'Виктория']

# with open('names.txt', 'r') as file:
#     for i in range(10):
#         file.write(names[random.randint(0, len(names) - 1)]+'\n')

with open('names.txt', 'r') as file:
    EOF = True
    while EOF:
        file_line = file.readline()
        name = file_line.strip('\n')
        if not name:  # если строка не пустая - то True, как только пустая строка(конец файла) то False
            EOF = False
        else:
            try:
                if len(name) < 5:
                    raise ValueError ("Длина имени меньше 5", name)

            except Exception as er:
                message, name = er.args[0], er.args[1]
                print(message + ': '+ name)



