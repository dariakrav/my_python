import random

def letter_game():
    s = ['самовар','весна','лето']
    word = random.choice(s)
    word1 =''.join(word)
    word1 = list(word1)
    letter = random.choice(word1)

    a = word.replace(letter, '?')
    print(a)
    b= input('Введите букву: ')
    if b != letter:
        print('Увы, попробйте в другой ращ')
    else:
        print('Победа!\nСлово: ')

letter_game()


