def str_n(string, n):
    if len(string) > n:
        return string.upper()
    else:
        return string

s = 'У Лукоморья дуб зеленый'

print(str_n(s, 7))