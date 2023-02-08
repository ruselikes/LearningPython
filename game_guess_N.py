from random import randint

win_number = randint(0,100)
attemps=0
print('Загаданное число',win_number)
while True:

    user_number = input('Введите число:')
    if not user_number.isdigit():
        print("Введите кореектное значение ЦЕЛОГО числа!")
        continue
    else:
        user_number = int(user_number)
        attemps +=1

    if user_number>win_number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif user_number<win_number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print(f"Вы угадали!Число попыток: {attemps}")
        break





