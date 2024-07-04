# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        ## DFS to find a path from root to p
        ## DFS to find a path from root to q
        ## compare the two paths
        ## return the last common node

        p_tree = self.dfs_helper(root, p)
        q_tree = self.dfs_helper(root, q)

        min_tree_len = len(p_tree) if len(p_tree) < len(q_tree) else len(q_tree)
        common_node = None

        for i in range(0, min_tree_len):
            if p_tree[i].val == q_tree[i].val:
                common_node = p_tree[i]

        return common_node

    def dfs_helper(self, root, p):
        if root is None:
            return None

        valid_path = [root]

        if root.val == p.val:
            return valid_path

        # curr_node = root
        left_tree = self.dfs_helper(root.left, p)
        right_tree = self.dfs_helper(root.right, p)

        if left_tree and right_tree:
            raise LookupError("Duplicate node values")
        elif left_tree:
            valid_path.extend(left_tree)
        elif right_tree:
            valid_path.extend(right_tree)
        else:
            return []

        return valid_path



if __name__ == '__main__':
    root_node = TreeNode(6)
    root_node.left = TreeNode(2)
    root_node.right = TreeNode(8)
    root_node.left.left = TreeNode(0)
    root_node.left.right = TreeNode(4)
    root_node.left.right.left = TreeNode(3)
    root_node.left.right.right = TreeNode(5)
    root_node.right.left = TreeNode(7)
    root_node.right.right = TreeNode(9)


    solution = Solution()
    print(solution.lowestCommonAncestor(root_node, TreeNode(0), TreeNode(9)).val)

    # print([i.val for i in solution.dfs_helper(root_node, TreeNode(100))])
