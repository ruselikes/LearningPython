import functools
from functools import reduce
# This is a sample Python script.
import calendar
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# x1,y1,x2,y2 = 1,2,5,6
# hipotenuze = ((x2 - x1)**2 + (y2-y1)**2)**0.5
# print(hipotenuze)

# num = (-10 + 2*(7**2+3/2)-3+3**(3**2)) / 3+4*10
# print(num)

# /num = int(input('Введите год '))
# if calendar.isleap(num):
#     print('Год високосный')
# else:
#     print('Год не високосный')

# str = input('url: ')
# if str.startswith("https") and 'documentlibrary' in str:
#     print('Адрес указан верно')
# elif not str.startswith("https"):
#     print('Ошибка: адрес не начинается с https.')
# else:
#     print('Ошибка: подстрока documentlibrary не обнаружена.')

# n = int(input('Введите число: '))
# for i in range(1,n+1,2):
#     print(f"{i}**5= {i**5}")

#password = input('Введите пароль:')
# for i in iter(int, 1):
#     if password == 'qwerty123':
#         print('Пароль верный!')
#         break
#     else:
#         print('Неверный пароль! Попробуйте ещё раз.')
#         password = input('Введите пароль:')


# n = 56;

# for i in range (2,int(n/2+1)):
#     if n % i == 0:
#         print(i)
#         for j in range(2, int(i / 2 + 1)):
#             if (i % j == 0):
#                 print(j)
#
# print('\n')




'''Напишите программу, которая создаёт список из квадратов чисел от 0 до 10 и выводит этот список на экран.
 Для создания списка используйте лямбда-функцию.'''
# sq_lst = [x **2 for x in range(10)]
# print(sq_lst)


'''Напишите программу, которая генерирует новый список из первого списка, заменяя все отрицательные числа на ноль.
 Для генерации используйте списочные выражения (list comprehensions).'''
# population_koefs = [1.1, -0.12, 3.12, -0.99, -2,22, 2.88, -2.92, 1.16, 4.2]
#
# new_koefs = [0 if x < 0 else x for x in population_koefs ]
# print(new_koefs)











