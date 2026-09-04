# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
    

        def recurFind(root, p, q):

            if root == None:
                return None

            a = p.val
            b = q.val
            x = root.val

            if a > x and b > x:
                return recurFind(root.right, p, q)

            elif a < x and b < x:
                return recurFind(root.left, p, q)
            
            elif ((a < x and b > x) or (a > x and b < x)):
                return root
            
            elif (x == a or x == b):
                return root

        
        res = recurFind(root, p, q)

        return res


           
