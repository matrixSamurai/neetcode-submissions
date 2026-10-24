# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isBalanced = True


        def dfs(root):

            nonlocal isBalanced

            if not root:
                return 0
            
            leftH = dfs(root.left)
            rightH = dfs(root.right)

            if abs(leftH - rightH) > 1:
                isBalanced = False
            
            return 1 + max(leftH, rightH)
        
        dfs(root)
        return isBalanced





        