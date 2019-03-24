
with open('text.txt', 'r') as reader, open('update_text.txt', 'a') as writer:
    for i, line in enumerate(reader,1):
        writer.write(f'{i} {line}')








