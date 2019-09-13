import array_worker as aw


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def selection_sort(array):
    for i in range(len(array)):
        min = i
        j = i + 1
        while j < len(array):
            if array[j] < array[min]:
                min = j
            j += 1
        array[i], array[min] = array[min], array[i]
    return array


b = aw.fill_array_random(7)
b = selection_sort(b)
for i in range(len(b)):
    print(b[i])
