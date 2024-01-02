<<<<<<< HEAD
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


list = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(list)

print("Sorted list:", list)
=======
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


list = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(list)

print("Sorted list:", list)
>>>>>>> 4ecb3844c2144b401961454300ba2506d47e26fa
