# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recur(root, leftMax, rightMax):

            if root is None:
                return True

            print(root.val, leftMax, rightMax)

            if leftMax >= root.val or rightMax <= root.val:
                return False
            
            return recur(root.left, leftMax, root.val) and recur(root.right, root.val, rightMax)


        return recur(root, -1 * 10000, 10000)
                    