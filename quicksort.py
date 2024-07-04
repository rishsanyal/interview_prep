
def quickSort(arr, smallerPtr, largerPtr):

    if smallerPtr >= largerPtr:
        return

    pivotElem = largerPtr

    ## Smaller looks for bigger element
    ## bigger ptr looks for smaller element

    while smallerPtr < largerPtr:
        while arr[smallerPtr] <= arr[pivotElem] and smallerPtr < pivotElem:
            smallerPtr += 1

        while arr[largerPtr] >= arr[pivotElem] and largerPtr > pivotElem:
            largerPtr -= 1

        if smallerPtr < largerPtr:
            arr[smallerPtr], arr[largerPtr] = arr[largerPtr], arr[smallerPtr]

    if arr[smallerPtr] > arr[pivotElem]:
        ## now we swap smallerPtr and PivotElem and return the recursion on both
        arr[smallerPtr], arr[pivotElem] = arr[pivotElem], arr[smallerPtr]

    quickSort(arr, smallerPtr, pivotElem - 1)
    quickSort(arr, pivotElem + 1, largerPtr)

if __name__ == "__main__":

    arr = [2,0,2,1,1,0] # [23,2,1,4, 3, 10, -1]

    smallerPtr = 0
    largerPtr = len(arr) - 1

    quickSort(arr, smallerPtr, largerPtr)

    print(arr)