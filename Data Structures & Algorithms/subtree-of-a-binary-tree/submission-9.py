# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def checkSubtree(root, subroot):

            if root == subroot:
                return True
            
            if not root or not subroot:
                return False
            
            if root.val != subroot.val:
                return False

            res1 = checkSubtree(root.left, subroot.left)
            res2 = checkSubtree(root.right, subroot.right)

            return res1 and res2


        def dfs(root):

            if root == subRoot:
                return True

            if not root or not subRoot:
                return False

            res1 = checkSubtree(root, subRoot)
            res2 = dfs(root.left)
            res3 = dfs(root.right)

            return res1 or res2 or res3
        
        return dfs(root)
        



        