data_list = [('Георгий', 'Невский проспект', 22), ('иван','пр. Ветеранов', 21 )]

def edit_tuple(file, list):
    with open(file, 'w') as output_text:
        output_text.write('name, address, age\n')
        for i in list:
            string =''.join(str(i))
            output_text.write(string + '\n')

edit_tuple('output.txt', data_list)
