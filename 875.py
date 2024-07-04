class Solution(object):
    def minEatingSpeed(self, piles, h):
        import math
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        ## Sort -> nlgn
        ## Binary search for the last successful number? nlgn

        if not piles:
            return 0

        # if len(piles) == 1:
        #     return piles[0]

        # sorted_piles = sorted(piles)

        def __check(curr_num):
            curr_hour_counter = 0

            for i in piles:
                curr_hour_counter += math.ceil(i / curr_num)

            return curr_hour_counter


        l, r = 1, max(piles)
        curr_hours = float('inf')

        # for midpoint in range(l, r+1):
        while l <= r:
            ## Get Midpoint
            ## We need to find the left-most element that works
            ## If mid works, we move left
            ## if mid don't work, we move right

            midpoint = (l + r) // 2

            temp_curr_hours = __check(midpoint)

            # if not curr_hours:
            #     curr_hours = midpoint

            if temp_curr_hours <= h:
                curr_hours = min(curr_hours, midpoint)
                r = midpoint - 1
            else:
                l = midpoint + 1

        return (curr_hours)


if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed([30,11,23,4,20], 5))
    # print(s.minEatingSpeed([3, 6, 7, 11], 8))
    # print(s.minEatingSpeed([312884470], 312884469))