# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def recurBalanced(root):

            if root == None:
                return 0

            leftTreeHeight = recurBalanced(root.left)
            rightTreeHeight = recurBalanced(root.right)

            if leftTreeHeight == -1 or rightTreeHeight == -1:
                return -1

            if abs(leftTreeHeight-rightTreeHeight) > 1:
                return -1

            return 1 + max(leftTreeHeight, rightTreeHeight)
        
        res = recurBalanced(root)

        if res != -1:
            return True
        else:
            return False

        