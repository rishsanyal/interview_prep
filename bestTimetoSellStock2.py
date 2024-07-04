class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # global currProfit
        currProfit = 0

        def _findAndAddProfit(tempPrices, currProfit):
            # Find index of Biggest element and Smallest Element before the
            # biggest element in tempPrices

            if not tempPrices or len(tempPrices) == 1:
                return

            smallestIndex = biggestIndex = 0
            currBiggestElement = currSmallestElement = None



            for i, j in enumerate(tempPrices):
                if not currBiggestElement:
                    currBiggestElement = j
                    biggestIndex = i

                if j > currBiggestElement:
                    currBiggestElement = j
                    biggestIndex = i


            for i, j in enumerate(tempPrices[:biggestIndex]):
                if not currSmallestElement:
                    currSmallestElement = j
                    smallestIndex = i

                if j < currSmallestElement:
                    currSmallestElement = j
                    smallestIndex = i

            if not currBiggestElement or not currSmallestElement:
                return 0

            currProfit += currBiggestElement - currSmallestElement

            print(currProfit)

            # _findAndAddProfit(tempPrices[:], currProfit)


        _findAndAddProfit(prices, currProfit)

        return currProfit


inputPrices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(inputPrices))
