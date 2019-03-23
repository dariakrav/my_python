import math

s = [2, 4, 9, 16, 25]


def roo_fun(list):
    a = []
    for i in list:
        value = math.sqrt(i)
        a.append(value)
    print(a)


roo_fun(s)

new_s = list(map(lambda i: math.sqrt(i), s))
print(new_s)

new_s1 = list(math.sqrt(i) for i in s)
print(new_s1)