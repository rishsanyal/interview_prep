# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        import math
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def constructBST(arr):
            if not arr or len(arr) == 0:
                return None
            # if startLen > endLen:
            #     return None

            # midpoint = math.ceil((endLen + startLen) / 2)
            midpoint = len(arr) // 2

            if midpoint < len(arr):
                tempNode = TreeNode(arr[midpoint])

                tempNode.left = constructBST(arr[0:midpoint])
                tempNode.right = constructBST(arr[midpoint + 1: len(arr)])

                return tempNode
            else:
                return None

        if not nums:
            return None

        else:
            return constructBST(nums)



    def bfs(self, root):
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
                elif node.left:
                    queue.append(node.left)
                elif node.right:
                    queue.append(node.right)
            res.append(level)
        return res


        # def checkHeightBalanced(self, root):

        #     if root is None:
        #         return 0

        #     leftHeight = self.checkHeightBalanced(root.left)
        #     if leftHeight == -1:
        #         return -1

        #     rightHeight = self.checkHeightBalanced(root.right)
        #     if rightHeight == -1:
        #         return -1

        #     heightDiff = leftHeight - rightHeight

        #     if abs(heightDiff) > 1:
        #         return -1
        #     else:
        #         return max(leftHeight, rightHeight) + 1


tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), None))
tempNode = Solution().sortedArrayToBST([1,2,3,4,5,6])

print(Solution().bfs(tempNode))