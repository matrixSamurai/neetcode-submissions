# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def recurb(root):

            if root == None:
                return 0

            depthLeft = recurb(root.left) + 1
            depthRight = recurb(root.right) +1

            return max(depthLeft, depthRight)


        result = recurb(root)
        
        return result


        