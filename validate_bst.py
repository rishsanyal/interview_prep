# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, lowLimit, highLimit):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or not root:
            return True
        elif root.left == None and root.right == None:
            # print(root.val)
            return True
        elif root.left == None and root.right > root.val:
            # print(root.right.val)
            return self.isValidBST(root.right, root.val, highLimit)
        elif root.right == None and root.left < root.val:
            # print(root.left.val)
            return self.isValidBST(root.left, lowLimit, root.val)
        else:
            # print(root.right)
            # print(self.isValidBST(root.right))
            # print(self.isValidBST(root.left))
            return (root.val > root.left.val and self.isValidBST(root.left, lowLimit, root.val)) and (root.val < root.right.val and self.isValidBST(root.right, root.val, highLimit))

        return False



def validateBST(self, root, low, high):
    if root is None:
        return True
    elif root.val < low or root.val > high:
        return False
    else:
        return self.validateBST(root.left, low, root.val) and self.validateBST(root.right, root.val, high)


