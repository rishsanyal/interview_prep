
from queue import Queue

# class NumObj(object):
#     def __init__(self, curr_num, curr_index, first_num, first_num_index, second_num, second_num_index, smallest_diff):
#         self.curr_num = curr_num
#         self.curr_index = curr_index
#         self.first_num = first_num
#         self.first_num_index = first_num_index
#         self.second_num = second_num
#         self.second_num_index = second_num_index
#         self.smallest_diff = smallest_diff

class Node(object):
    def __init__(self, val, index, diff, next_node = None):
        self.val = val
        self.index = index
        self.curr_smallest_diff = diff
        self.next = next_node

class Solution():
    def __init__(self):
        self.node = None

    # def insert_node(self, i, val):
    #     curr_node = self.node
    #     tempNode = Node(val, i, 0)

    #     next_node = None

    #     while curr_node:
    #         if val < curr_node.val:
    #             next_node = curr_node
    #             curr_node = tempNode
    #             curr_node.next = next_node
    #             self.node = curr_node
    #         else:
    #             next_node = curr_node
    #             curr_node = curr_node.next

    #     if not curr_node:
    #         next_node.next = tempNode


    #     return None

    def count(self, nums, k):

        if len(nums) == 0:
            return

        q = Queue(k)
        res = []

        first_num, first_num_index = None, None
        second_num, second_num_index = None, None
        third_num, third_num_index = None, None

        for i, val in enumerate(nums):
            if q.full():
                pop_val, pop_index = q.get()
                q.put((val, i))

            if (not first_num or not second_num or not third_num):
                if not first_num:
                    first_num, first_num_index = val, i
                    res.append(val)
                elif not second_num:
                    if val > first_num:
                        second_num, second_num_index = val, i
                    else:
                        second_num, second_num_index = first_num, first_num_index
                        first_num, first_num_index = val, i

                    res.append((second_num - first_num))
                elif not third_num:
                    ## Compare with first_num
                    ## Compare with second_num
                    ## else: assign to third num
                    if val < first_num:
                        third_num, third_num_index = second_num, second_num_index
                        second_num, second_num_index = first_num, first_num_index
                        first_num, first_num_index = val, i
                    elif val < second_num:
                        third_num, third_num_index = second_num, second_num_index
                        second_num, second_num_index = val, i
                    else:
                        third_num, third_num_index = val, i

                    if not third_num:
                        res.append((second_num - first_num))
                    else:
                        res.append(min((second_num - first_num), (third_num - second_num)))

                q.put((val, i))
            else:
                ## pop from queue

                ## Assign None to relevant number
                ## Move number up
                    ## If it's first num that's popped then 2nd becomes first, 3rd becomes second, etc
                    ## If it's second that's popped then third becomes 2nd
                    ## if it's third then we're good

                if pop_index == first_num_index:
                    first_num, first_num_index = second_num, second_num_index
                    second_num, second_num_index = third_num, third_num_index
                    third_num, third_num_index = None, None
                elif pop_index == second_num_index:
                    second_num, second_num_index = third_num, third_num_index
                    third_num, third_num_index = None, None
                else:
                    third_num, third_num_index = None, None

                if val < first_num:
                    third_num, third_num_index = second_num, second_num_index
                    second_num, second_num_index = first_num, first_num_index
                    first_num, first_num_index = val, i
                elif val < second_num:
                    third_num, third_num_index = second_num, second_num_index
                    second_num, second_num_index = val, i
                else:
                    third_num, third_num_index = val, i
                ## Then we compare against all three
                ## if val < first_num
                ## elif val < second_num
                ## else: third_num, thid_num_index = val, i (Third num is free at this point anyway)
                res.append(min((second_num - first_num), (third_num - second_num)))

                print(second_num)
                print(first_num)
            #     ## Then we append the min diff to res

        print(res)


if __name__ == '__main__':
    # Find the minimum absolute difference possible between 2 in a queue of size N
    # if curr_num < smallest_num:

    nums = [1, 2, 8, 4, 7]
    k = 3

    s = Solution()

    print(s.count(nums, k))
