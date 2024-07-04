# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # visited = defaultdict(lambda: 0)

        if not root:
            return 0

        def alternate_traverse(curr_node, prev_turn, curr_depth):

            curr_temp_node, curr_len = curr_node, curr_depth

            if curr_temp_node is None:
                return curr_depth
            else:
                if prev_turn == 'L':
                    depth = max(
                        curr_depth,
                        alternate_traverse(curr_temp_node.right, 'R', curr_len+1),
                        alternate_traverse(curr_temp_node.left, 'L', 0)
                    )

                if prev_turn == 'R':
                    depth = max(
                        curr_depth,
                        alternate_traverse(curr_temp_node.left, 'L', curr_len+1),
                        alternate_traverse(curr_temp_node.right, 'R', 0)
                    )

                return depth


        return max(alternate_traverse(root.left, 'L', 0), alternate_traverse(root.right, 'R', 0))


