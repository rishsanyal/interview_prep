class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """


        result = []

        # intervals_to_merge.append(newInterval)

        for i in range(0, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        result.append(newInterval)

        return result





s = Solution()
# s.insert([[1,3], [6,9]], [2,5])
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# s.insert([[1,5]], [0,3])