s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"

def un_delete(string):
    new_string = string.split(' ')
    for i in new_string:
        if i.startswith('м') or i.startswith('М') :
            new_string.remove(i)
        else:
            continue
    print(new_string)

un_delete(s)