example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    n = len(data)
    for i in range(n-1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break

    return data


print(bubble_sort(example_array))