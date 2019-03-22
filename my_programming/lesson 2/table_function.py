



def table_function():
    number = int(input('Введите, пожалуйста значение, которое вы хотите проверить:'))
    if number == 80:
        print('Это Mn - марганец')
    elif 0 < number < 2:
        print('Это элемент первого периода ')
    elif 2 < number < 11 and number == 3:
        print('Это Li - литий ')
    elif 2 < number < 11:
        print('Это элемент второго периода ')
    elif 10 < number < 19 and number == 17:
        print('Это Cl - хлор ')
    elif 10 < number < 19:
        print('Это элемент третьего периода')
    elif 18 < number < 37:
        print('Это элемент четвертого периода')

    else:
        print('Извините, я не знаю, что это за элемент')

table_function()