# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        global ans
        ans = 0

        def traverse(node):

            left_path = 0
            right_path = 0
            global ans

            if node.left is not None:
                left_path = traverse(node.left)

            if node.right is not None:
                right_path = traverse(node.right)

            if left_path + right_path > ans:
                ans = left_path + right_path

            return max(left_path, right_path) + 1

        traverse(root)

        return ans