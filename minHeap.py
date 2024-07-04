# All parents are smaller than their children nodes.
# We could use nodes but we could also use an Array


class MinHeapArray():

    def __init__(self):
        self.arr = []
        self.size = 0
        self.capacity = 10

    # Check Size of array
    def checkSize(self):
        if len(self.arr) <= self.capacity:
            return True

        tempArr = [None]*(self.capacity*2)
        self.size = len(tempArr)
        tempArr[0:len(self.arr)] = self.arr
        self.arr = tempArr

        return False


    # getLeftChildIndex
    # getRightChildIndex
    # getParentIndex

    # getRightChildValue
    # getLeftChildValue
    # getParentValue

    # hasLeftChild
    # hasRightChild
    # hasParent

