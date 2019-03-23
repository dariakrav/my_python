import random
import math


def game():
    attempts = 5
    while attempts > 0:
        number = random.randint(1, 100)
        user_answer = int(input('Введите число: '))
        if user_answer == number:
            print('Победа')
        elif user_answer != number and user_answer > number:
            print('Ваше число больше загаданного')
        elif user_answer != number and user_answer < number:
            print('Ваше число меньше загаданного')
        attempts = attempts -1
        print('Ваше количество попыток - ', attempts)


game()