class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        ## Getting available spots
        ## num of 3 0's

        if n == 0:
            return True

        if len(flowerbed) == 0:
            return False

        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1 or n == 0:
                return True
            return False

            # we can only plant 2 if [0, 0, 0]
            # we can only plan 1 if [1, 0, 0] or [0, 0, 1]
            # we can plant 0 if [0, 1, 0]

        availableSpots = 0
        i = 0

        oldN = n

        while i < len(flowerbed) and oldN > 0:
            if flowerbed[i] == 0:
                if i - 1 < 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        availableSpots += 1
                        oldN -= 1
                else:
                    if i + 1 < len(flowerbed):
                        if (flowerbed[i-1] == 0)  and (flowerbed[i+1] == 0):
                            flowerbed[i] = 1
                            availableSpots += 1
                            oldN -= 1
                    else:
                        if (flowerbed[i-1] == 0):
                            flowerbed[i] = 1
                            availableSpots += 1
                            oldN -= 1


                # else:
                #     if (flowerbed[i-1] == 0)  and (flowerbed[i+1] == 0):
                #         flowerbed[i] = 1
                #         availableSpots += 1
                #         oldN -= 1

            i += 1


        print(flowerbed)

        print(availableSpots)
        print(n)

        return availableSpots == n


        ## if currFlowerbed == 1, nextSpot = i + 2, if i+2 == 0
        ## if currFlowerbed == 0 and i+1 and i-1 != 1, plant


### Beautiful solution

# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         count = 0
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0:
#                 empty_left_plot = (i==0) or (flowerbed[i-1] == 0)
#                 empty_right_plot = (i==len(flowerbed)-1) or (flowerbed[i+1] == 0)

#                 if empty_left_plot and empty_right_plot:
#                     flowerbed[i] = 1
#                     count += 1
#         return count >= n



s = Solution()
print(s.canPlaceFlowers([1,0,0,0,0,1], 2))
print(s.canPlaceFlowers([0,0,0,0,0], 3))
print(s.canPlaceFlowers([0, 0], 2))