class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)

# def get_nth_from_end(head, n):

#     if head is None:
#         return

#     currHead = head
#     currNext = head.next
#     i = 0

#     get_nth_from_end(currNext, n)

#     i += 1
#     if i == n:
#         return currHead.data


def printNthFromLast(head, N):


    def get_nth_from_end(head, n, prevNode=None):
        if (head == None):
            return 0

        temp = get_nth_from_end(head.next, n, head)

        if (temp == n):
            if prevNode:
                prevNode.next = head.next
        return temp + 1

    tempVal = get_nth_from_end(head, N)

    if tempVal == N:
        head = head.next

    return head


def print_linked_list(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

def print_linked_list_in_reverse(head, inputList=[]):
    if head.next is None:
        inputList.append(head.data)
        return head.data == inputList[-1]

    inputList.append(head.data)

    if print_linked_list_in_reverse(head.next, inputList):
        print(head.data)
        print(inputList[-1])
        return True
    return False


def print_half_linked_list(head):
    slow = head
    fast = head
    prevSlow = None
    isOdd = False

    while fast is not None and fast.next is not None:
        prevSlow = slow
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        isOdd = True
        slow = slow.next

    while slow is not None:
        print(slow.data)
        slow = slow.next



headNode = Node(5)
headNode.next = Node(4)
headNode.next.next = Node(3)
headNode.next.next.next = Node(4)
headNode.next.next.next.next = Node(5)


# printNthFromLast(headNode, 2)

# print_linked_list(headNode)
# print(print_linked_list_in_reverse(headNode))

print_half_linked_list(headNode)