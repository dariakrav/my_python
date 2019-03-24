
temperatures = []
with open('temper.stat') as infile:
    for row in infile:
        temperatures.append(float(row))

print('Максимальное значение данной выборки {}'.format(max(temperatures)))
print(f'Минимальное значение данной выборки {min(temperatures)}')

print('Среднее значение данной выборки {}'.format(sum(temperatures)/len(temperatures)))
print(f'Медиана данной выборки {len(temperatures)//2}')

