# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        def recurTraverse(root, levelList, level):

            if root == None:
                return

            # This is the important thing to remember to add the empty list in the list 
            # before adding any elelment to it, and we do it by checking the level 
            # by the length of the list.
            if level == len(levelList):
                levelList.append([])
            
            # Adding the value to the list before making the new recursive calls, this
            # is also very important, as we need to append the root only before the 
            # new recursion calls
            levelList[level].append(root.val)

            recurTraverse(root.left, levelList, level + 1)
            recurTraverse(root.right, levelList, level + 1)

        
        levelList = []
        recurTraverse(root, levelList, 0)

        return levelList

