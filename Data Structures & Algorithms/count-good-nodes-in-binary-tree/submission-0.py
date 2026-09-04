# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def recur(root, maxAbove):

            if root == None:
                return 0
            
            if root.val >= maxAbove:
                return 1 + recur(root.left, root.val) + recur(root.right, root.val)
            else:
                return recur(root.left, maxAbove) + recur(root.right, maxAbove)

        
        result = recur(root, -1 * 10**100)

        return result

        