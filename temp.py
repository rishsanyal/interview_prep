def quicksort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, r)


def partition(arr, l, r):
    pivot = r

    i = l
    j = r

    while i < j:
        while arr[i] <= arr[pivot] and i < r:
            i += 1
        while arr[j] >= arr[pivot] and j > l:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] >= arr[pivot]:
        arr[i], arr[pivot] = arr[pivot], arr[i]

    return i

if __name__ == "__main__":
    arr = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]
    quicksort(arr, 0, len(arr)-1)
    print(arr)