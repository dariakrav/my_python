print(pow(12,4))

print(round(1.23325346, 2))

a = pow(abs(-5.343653) + abs(-3.3463472), round(5.6))

print(a)

def calculate(x):
    return pow(x,4)+ pow(4,x)

print(calculate(18))

def quad(c):
    return 4*c

def farenh_to_calculate(x):
    return x*9/5 + 32

farenh_to_calculate(5)

def delete(a,b):
    return a/b

def sum(a,b,c):
    return a+b+c

def average(a,b,c):
    return delete(sum(a,b,c),3)

average(2,7,19)

def test_pow(a,b,c):
    print(pow(sum(a,b,c),2))

test_pow(20,12,1)

st = 'I need a glass of water'
print(st[::3])


sp = 'Hell0'

print('Привет, ' + input('Как тебе зовут, мальчик?\n') + '!\n')

print('Здравствуй, дорогой друг!')
age = input('Скажи, пожалуйста, сколько тебе сейчас лет?\n')
future_age = int(age) + 1
print('Значит, в следующем году тебе будет ' + str(future_age))
