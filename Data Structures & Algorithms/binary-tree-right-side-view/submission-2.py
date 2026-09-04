# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideViewMysolution(self, root: Optional[TreeNode]) -> List[int]:

        def recur(root, level, resList):

            if root == None:
                return 
            
            if level == len(resList):
                resList.append([])

            resList[level].append(root.val)
            

            recur(root.left, level+1,  resList)
            recur(root.right, level+1,  resList)

        
        resList = []
        ansList = []
        
        recur(root, 0, resList)

        for levelList in resList:
            ansList.append(levelList[len(levelList) -1])

        return ansList
    

    # This one is the best and the optimal soltuion
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = [] 

        def recur(root, level):

            if root == None:
                return

            if level == len(res):
                res.append(root.val)

            recur(root.right, level + 1)
            recur(root.left, level + 1)
        
        recur(root,0)

        return res



            

            



        
        