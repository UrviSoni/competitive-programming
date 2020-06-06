# Invert a binary tree.
#         
#        4                          4
#      /   \                      /   \
#     2     7        == >        7     2
#    / \   / \                  / \   / \
#   1   3 6   9                9   6 3   1
#
# [4,2,7,1,3,6,9]             [4,7,2,9,6,3,1]
#
#     Input                        Output


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        r = self.invertTree(root.right)
        l = self.invertTree(root.left)
        
        root.right = l
        root.left = r
        
        return root
