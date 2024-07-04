
def merge(arr, low, medium, high):

    tempLeft = []
    tempRight = []
    finalArr = []

    for i in range(low, medium):
        tempLeft.append(arr[i])

    for j in range(medium, high):
        tempRight.append(arr[j])

    i, j, k = 0, 0, 0

    while i < len(tempLeft) and j < len(tempRight):
        if tempLeft[i] < tempRight[j]:
            finalArr.append(tempLeft[i])
            i += 1
        else: # tempRight[j] < tempLeft[i]:
            finalArr.append(tempRight[j])
            j += 1
        k += 1


    while i < len(tempLeft):
        finalArr.append(tempLeft[i])
        i += 1

    while j < len(tempRight):
        finalArr.append(tempRight[j])
        j += 1

    # print(finalArr)

    return finalArr

def mergesort(arr, low, high):
    if low < high - 1:
        middlePoint = (low + high) // 2

        mergesort(arr, low, middlePoint)
        mergesort(arr, middlePoint, high)

        arr[low:high] = merge(arr, low, middlePoint, high)

if __name__ == "__main__":

    # arr = [23,2,1,4, 3, 10, -1]
    arr = [2,0,2,1,1,0]

    smallerPtr = 0
    largerPtr = len(arr)

    mergesort(arr, smallerPtr, largerPtr)

    print(arr)