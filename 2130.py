# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        ## First node, last node

        ## We can override the ListNode object to have numbers
        ## Assign the numbers and find the twin

        ## get last node number
        ## modify the linked list to not have a last node

        ### WINNER:
        ### Reverse second half of list
        ### Add head of first list and head of reversed list



        ### Get middle node
        ### Reverse from that point onwards
        ### Track it and sum everything up

        prev_node = None

        curr_head = head
        curr = head
        middle_node = head

        while curr.next and curr.next.next:
            prev_node = middle_node
            middle_node = middle_node.next
            curr = curr.next.next


        def __reverse_list(curr_node, prev_node):

            last_node = curr_node

            curr_head, next_node = curr_node, curr_node
            curr_prev_node = prev_node

            while curr_head:
                next_node = curr_head.next

                curr_head.next = curr_prev_node

                curr_prev_node = curr_head
                curr_head = next_node

            # print(curr_prev_node.next)
            last_node.next = None

            return curr_prev_node




        if middle_node:
            middle_node.next = __reverse_list(middle_node.next, middle_node)
        else:
            middle_node = head

        max_twin_sum = 0

        # print(middle_node.val)

        while middle_node.next:
            curr_twin_sum = curr_head.val +  middle_node.next.val
            if curr_twin_sum > max_twin_sum:
                max_twin_sum = curr_twin_sum
            middle_node = middle_node.next
            curr_head = curr_head.next

        return max_twin_sum


s = Solution()

# inp = [47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9]

inp = [2,3,5,4,8,6]

start = None
head = None

for i in inp:
    if start is None:
        start = ListNode(i)
        head = start
    else:
        start.next = ListNode(i)
        start = start.next


print(s.pairSum(head))
