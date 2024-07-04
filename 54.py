from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []

        result = []

        left, right=  0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            ## Go right
            for i in range(left, right):
                result.append(
                    matrix[top][i]
                )

            top += 1

            # GO down
            for i in range(top, bottom):
                result.append(
                    matrix[i][right-1]
                )

            right -= 1

            if not (left < right and top < bottom):
                break

            # Go left
            for i in range(right-1, left-1, -1):
                result.append(
                    matrix[bottom-1][i]
                )

            bottom -= 1

            # Go up
            for i in range(bottom-1, top-1, -1):
                result.append(
                    matrix[i][left]
                )

            left += 1

        return result

s = Solution()
# print(s.spiralOrder([[6, 9]]))
# print(s.spiralOrder([[3],[2]]))
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
x = s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(len(x) == len(set(x)))

print(x)