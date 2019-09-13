import array_worker as aw


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


b = aw.fill_array_random(20)
b = bubble_sort(b)
for i in range(len(b)):
    print(b[i])
