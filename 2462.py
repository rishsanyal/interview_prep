import heapq


class Solution(object):
    def totalCost(self, costs, k, n):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """

        ## -> 1 worker per session
        ## -> We can only pick from the first N workers or the last N workers
        ## -> if we have the same cost of labor, we break the tie with the index
        ## -> If there are less than N candidates remaining, we pick the one with the
        ##    lowest cost and the lowest index

        total_cost = 0
        remaining_list = []

        heap1, heap2 = [], []

        if len(costs) >= n:
            heap1 = costs[:n]

            if len(costs) - n >= n:
                heap2 = costs[len(costs)-n:]
                remaining_list = costs[n:len(costs)-n]
            else:
                heap2 = costs[n:]
                remaining_list = []

            heapq.heapify(heap1)
            heapq.heapify(heap2)


        for i in range(k):
            if heap1 and heap2:

                print(heap1, heap2)

                staff_from_heap1 = heapq.nsmallest(1, heap1)[0]
                staff_from_heap2 = heapq.nsmallest(1, heap2)[0]

                # print(staff_from_heap1, staff_from_heap2)


                if staff_from_heap1 > staff_from_heap2:
                    heapq.heappop(heap2)
                    total_cost += staff_from_heap2

                    # costs = heap1 + remaining_list + heap2
                    if remaining_list:
                        heapq.heappush(heap2, remaining_list.pop(-1))
                        print(heap2)

                else:
                    heapq.heappop(heap1)
                    total_cost += staff_from_heap1

                    if remaining_list:
                        heapq.heappush(heap1, remaining_list.pop(0))
                        print(heap1)




            else:
                print("Here please")
                heap1 = heap1 + heap2
                heapq.heapify(heap1)
                total_cost += heapq.heappop(heap1)

            # costs = heap1 + remaining_list + heap2

        return total_cost




s = Solution()

# costs = [17,12,10,2,7,2,11,20,8]
# costs = [1,2,4,1]
costs = [69,10,63,24,1,71,55,46,4,61,78,21,85,52,83,77,42,21,73,2,80,99,98,89,55,94,63,50,43,62,14]


k = 21
candidates = 31


print(s.totalCost(costs, k, candidates))