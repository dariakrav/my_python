s = 'У лукоморья 123 дуб зеленый 456'

print(s.find('я'))
print(s.count('у'))

if not s.isalpha():
    print(s.upper())

if len(s) > 4:
    print(s.lower())

s = list(s)
s[0] = 'О'
s = ''.join(s)
print(s)


