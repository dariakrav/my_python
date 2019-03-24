import random
numbers = [random.randint(-100, 100) for i in range(999)]
print(numbers)

def min_function(list):
    value_count = 0
    for value in list:
        min_list_position = list.index(min(list))
        max_list_position = list.index(max(list))
        if min_list_position <= list.index(value) <= max_list_position and value <0:
            value_count += 1
    print(value_count)


min_function(numbers)