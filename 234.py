# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def reverse(self, midPtr, prevPtr):

        while midPtr:
            currPtr = midPtr
            nextPtr = currPtr.next

            currPtr.next = prevPtr

            prevPtr = currPtr
            midPtr = nextPtr

        return prevPtr

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slowPtr, fastPtr = head, head

        tempHead = head

        while fastPtr:
            if fastPtr.next and fastPtr.next.next:
                fastPtr = fastPtr.next.next
                slowPtr = slowPtr.next
            elif fastPtr.next:
                fastPtr = fastPtr.next
                slowPtr = slowPtr.next
            else:
                break

        ## Reverse the linked list from fastPtr to slowPtr
        tempNode = self.reverse(slowPtr.next, slowPtr)

        slowPtr.next = None

        while tempNode and tempNode:
            if tempHead.val != tempNode.val:
                return False
            tempHead = tempHead.next
            tempNode = tempNode.next

        return True



if __name__ == '__main__':
    s = Solution()

    t = ListNode(1)
    t.next = ListNode(2)
    t.next.next = ListNode(2)
    t.next.next.next = ListNode(1)
    # t.next.next.next.next = ListNode(1)

    print(s.isPalindrome(t))