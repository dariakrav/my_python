import os

print(os.listdir())

file = open('example_text.txt', 'r')
contents = file.readlines()
print(contents)

file.close()

with open('plan.txt') as plan:
    planets = plan.readlines()
    planets = sorted(planets)

for planet in planets:
    print(planet.strip())


with open('sort_plan.txt', 'w') as new_plan:
    for planet in planets:
        new_plan.write(planet)

def file_writeline(file, list):
    try:
        with open(file, 'w') as file_line:
            file_line.writelines(list)
        print('данные записаны')
    except Exception as e:
        print(e)


ss = ['Planets\n', 'Asteroids\n', 'Stars\n']
file_writeline('plan.txt', ss )

path = 'dogs_breed.txt'
path_new = 'dogs_breed_reversed.txt'

with open(path, 'r') as reader, open(path_new, 'w') as writer:
    dogs_breeds = reader.readlines()
    writer.writelines(reversed(dogs_breeds))