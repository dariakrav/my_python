import random

def game():
    print('Мы загадали однозначное число и предлагаем вам попробовать его отгадать')
    number = int(input('Введите число:'))
    our_number = random.randint(1,4)
    if number == our_number:
        print('Победа')
    elif number > our_number:
        print('Ваше число больше загаданного')
        print('Повторите еще раз')

    else:
        print('Ваше число меньше загаданного')
        print('Повторите еще раз')

    return number

game()