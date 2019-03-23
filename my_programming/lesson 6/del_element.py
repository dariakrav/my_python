
names = ['John', 'Paul', 'George', 'Ringo']
new_names = list(filter(lambda x: x !='George' and x != 'Ringo', names))
print(new_names)