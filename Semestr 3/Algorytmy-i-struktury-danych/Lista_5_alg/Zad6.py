def quicksort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        pivot_index = partition(arr, low, high)

        if pivot_index - 1 > low:
            stack.append((low, pivot_index - 1))

        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))

    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quicksort(arr)
print(arr)
