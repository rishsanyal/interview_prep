# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        ## We have two ListNodes -> Odd, Even
        ## Both of them will be fast pointers

        if not head or not head.next:
            return head

        ## Create odd and even Nodes
        odd, even = ListNode(), ListNode()
        odd_head, even_head = odd, even

        ## Iterate through the linkedlist and split into odd and even nodes
        while head:
            odd.next = head
            odd = odd.next

            if head.next:
                even.next = head.next
                even = even.next

            if head.next:
                if head.next.next:
                    head = head.next.next
                else:
                    head = None

                odd.next = None

                if even:
                    even.next = None
            else:
                head = None

        lastOdd = None

        while odd:
            lastOdd = odd
            odd = odd.next

        lastOdd.next = even_head.next

        return odd_head.next








# if not head or not head.next or not head.next.next:
#             return head

#         p1 = head
#         p2 = head.next
#         start = head.next
#         while p2 and p2.next:
#             p3 = p2.next.next
#             p1.next = p2.next
#             p1 = p1.next

#             p1.next = start
#             p2.next = p3
#             p2 = p2.next
#         return head