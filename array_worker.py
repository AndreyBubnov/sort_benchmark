import random
def fill_array_standart(array_len):
    array = []
    for i in range(array_len):
        array.append(i)
    return array

def fill_array_reverse(array_len):
    array = []
    for i in range(array_len):
        array.append(array_len - i)
    return array

def fill_array_random(array_len):
    array = []
    for i in range(array_len):
        array.append(random.randint(0, array_len))
    return array