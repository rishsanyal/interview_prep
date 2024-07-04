def quicksort(arr, left, right):

    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)

    return None

def partition(arr, left, right):
    i = left
    j = right - 1

    pivot = right

    while i < j:
        while arr[i] <= arr[pivot] and i < right:
            i += 1
        while arr[j] >= arr[pivot] and j > left:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > arr[pivot]:
        arr[i], arr[right] = arr[right], arr[i]

    return i


if __name__ == "__main__":
    arr = [1, 2, 3, 0]
    # arr = [0,0,1,0,1,1]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)



