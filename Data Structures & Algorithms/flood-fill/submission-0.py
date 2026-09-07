class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        visit = set()
        ROW, COL = len(image), len(image[0])

        def dfs(r, c, oldColor, newColor):


            if min(r,c)< 0 or r== ROW or c== COL or image[r][c] != oldColor or (r,c) in visit:
                return
            
            image[r][c] = newColor
            visit.add((r,c))

            dfs(r-1,c, oldColor, newColor)
            dfs(r+1,c, oldColor, newColor)
            dfs(r,c+1, oldColor, newColor)
            dfs(r,c-1, oldColor, newColor)

        
        dfs(sr, sc, image[sr][sc], color)

        return image
        