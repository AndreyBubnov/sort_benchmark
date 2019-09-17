import array_worker as aw


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                aw.swap(array, j, j + 1)
    return array


def selection_sort(array):
    for i in range(len(array)):
        min = i
        j = i + 1
        while j < len(array):
            if array[j] < array[min]:
                min = j
            j += 1
        aw.swap(array, i, min)
    return array


def insertion_sort(array):
    for i in range(len(array)):
        tmp = array[i]
        j = i - 1
        while j >= 0 and tmp < array[j]:
            aw.swap(array, j, j + 1)
            j -= 1
    return array


def shaker_sort(array):
    while True:
        for i in (range(len(array) - 1), reversed(range(len(array) - 1))):
            swapped = False
            for j in i:
                if array[j] > array[j + 1]:
                    aw.swap(array, j, j + 1)
                    swapped = True
            if not swapped:
                return array


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        i = aw.random.choice(array)
        left = []
        middle = []
        right = []
        for elem in array:
            if elem < i:
                left.append(elem)
            elif elem > i:
                right.append(elem)
            else:
                middle.append(elem)
        return quick_sort(left) + middle + quick_sort(right)


def heap_sort(array):
    def heapify(array, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2
        if left_child < heap_size and array[left_child] > array[largest]:
            largest = left_child
        if right_child < heap_size and array[right_child] > array[largest]:
            largest = right_child
        if largest != root_index:
            aw.swap(array, root_index, largest)
            heapify(array, heap_size, largest)
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        aw.swap(array, i, 0)
        heapify(array, i, 0)
    return array


b = aw.fill_array_random(10)
b = heap_sort(b)
for i in range(len(b)):
    print(b[i])
