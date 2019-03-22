rabbits = 3

n = [1,2,34,2,3,1,6,6,7,5]

a = 'tweak the problem when you see the glimpse of it see'
lst = a.split(' ')


def find_wor(s):
    find_word = dict()
    for word in s:
        find_word.setdefault(word, 0)
        find_word[word] += 1
    return find_word

print(find_wor(lst))

def funct(list):
    d= {}
    for i in list:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print(funct(n))



while rabbits >0:
    print(rabbits)
    rabbits = rabbits - 1

list = [1,23,-1,5]
result = 0

for i in list:
    if i < 0:
        break
    result += i
print(result)