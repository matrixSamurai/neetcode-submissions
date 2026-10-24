# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(rootA, rootB):

            if rootA == rootB:
                return True
            
            if not rootA or not rootB:
                return False
            
            checkLeft = dfs(rootA.left, rootB.left)
            checkRight = dfs(rootA.right, rootB.right)

            if rootA.val != rootB.val:
                return False
            
            return checkLeft and checkRight
        
        return dfs(p, q)
    

        

        