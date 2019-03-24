list = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]

def find_smallest(list):
    smallest = min(list)
    min1 = list.index(smallest)
    list.remove(smallest)

    second_smallest = min(list)
    min2 = list.index(second_smallest)

    list.insert(min1, smallest)

    if min1 <= min2:
        min2 +=1
    return (min1, min2)

print(find_smallest(list))

