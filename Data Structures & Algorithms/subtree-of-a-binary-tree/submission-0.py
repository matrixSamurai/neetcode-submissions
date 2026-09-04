# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def actualRecur(root, subroot):

            if root == None and subroot == None:
                return True
            elif root == None or subroot == None:
                return False

            leftSearch = actualRecur(root.left, subroot.left)
            rightSearch = actualRecur(root.right, subroot.right)

            if root.val == subroot.val:
                return leftSearch and rightSearch
            else:
                return False



        def startFindRecur(root, subroot):

            if root == None:
                return False

            leftRoot = startFindRecur(root.left, subroot)
            rightRoot = startFindRecur(root.right, subroot)

            if root.val == subroot.val:
                return actualRecur(root, subroot) or leftRoot or rightRoot
            else:
                return leftRoot or rightRoot


        res = startFindRecur(root, subRoot)
        return res

