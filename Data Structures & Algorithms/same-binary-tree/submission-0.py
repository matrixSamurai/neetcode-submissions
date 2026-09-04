# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def recurIsSame(rootP, rootQ):

            if rootP == None and rootQ == None:
                return True
            elif rootP == None or rootQ == None:
                return False


            isLeftSame = recurIsSame(rootP.left, rootQ.left)
            isRightSame =  recurIsSame(rootP.right, rootQ.right)


            if rootP.val == rootQ.val and isLeftSame and isRightSame:
                return True
            else:
                return False

        res = recurIsSame(p, q)

        return res
        

        