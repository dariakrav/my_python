import math


o = [1,3,4]
O=[i*4 for i in o]
print(O)

L = [3,6,7,4,-5,4,3,-1]

n = [1,2,4,5,6,8,9,10]

print([i for i in L if i in n])

n[1::2] = [0]*len(n[1::2])

print(n)

def intersect(list1,list2):
    list =[]
    for value1 in list1:
        if value1 in list2:
            list.append(value1)
    return list

print(intersect(L, n))





def div(list):
    if (abs(max(list)) - abs(min(list))) > 10:
        print(sorted(L))
    else:
        print('The difference is less than 10')

div(L)

def element_sum(list):
    summed = sum(list)
    if summed >2:
        print(len(list))
    else:
        print('Sum of list is not bigger than 2')

element_sum(L)

s = [3, 'hello', 7, 4, 34, 4, 5, -1, 'привет']

def unsure():
    if 'привет' in s:
        s.remove('привет')
    else:
        s.append('привет')

print(unsure())

print(s[::2])

if 'привет' in s:
    print('привет'*10)

print(s)
print(round(math.pi, 2))

def is_palindrome(word):
    if word == word[::-1]:
        print('The word is palindrome')
    else:
        print('What the fuck is that word doing here?')

is_palindrome('shit')


def absolute(a):
    if a>0:
        return a
    else:
        return -a

print(absolute(-2))

value = input('Введите pH: ')
if value:
    pH = float(value)
    if pH == 7.0:
        print('Вода')
    elif 7.36 < pH < 7.44:
        print('Кровь')
    else:
        print('Что это такое?')
else:
    print('Введите значение pH!')



print(6==5, '\n')

print(5==5 or 3==2)

print(ord('A'))
print(ord('X'))

print('A'>'X')
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
num_sum = num1 + num2 + num3
print('Сумма введенных чисел: ' + str(num_sum))
dis_sum = num1*num2*num3
print('Произведение введенных чисел: ' + str(dis_sum))

