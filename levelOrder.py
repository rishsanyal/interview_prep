# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def createLevelList(root, finalList=[]):
            if root is None:
                return finalList

            elif root.left != None and root.right != None:
                finalList.append([root.left.val, root.right.val])
                createLevelList(root.left, finalList)
                createLevelList(root.right, finalList)

            elif root.left != None:
                finalList.append([root.left.val])
                createLevelList(root.left, finalList)

            elif root.right != None:
                finalList.append([root.right.val])
                createLevelList(root.right, finalList)

            return finalList

        if root != None:
            return [[root.val]] + createLevelList(root)

        return []


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

    def checkHeightBalanced(self, root):

        if root is None:
            return 0

        leftHeight = self.checkHeightBalanced(root.left)
        if leftHeight == -1:
            return -1

        rightHeight = self.checkHeightBalanced(root.right)
        if rightHeight == -1:
            return -1

        heightDiff = leftHeight - rightHeight

        if abs(heightDiff) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1


# tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree = TreeNode(3, None, None)

# print(Solution().bfs(tree))

print(Solution().checkHeight(tree))