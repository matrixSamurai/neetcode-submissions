# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

#         def dfs(i,j,grid):

#             if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
#                 return 0
        
#             if grid[i][j] == 1:
#                 grid[i][j] = 0
#                 return 1 + dfs(i+1,j,grid) + dfs(i,j+1,grid) + dfs(i-1,j,grid) + dfs(i,j-1,grid)
#             else:
#                 return 0
        

#         maxArea = 0

#         for i in range(0, len(grid)):
#             for j in range(0, len(grid[0])):
#                 if grid[i][j] == 1:
#                     localMax = dfs(i,j,grid)
#                     if localMax > maxArea:
#                         maxArea = localMax
#                         print(maxArea)

#         return maxArea


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visit = set()
        ROW, COL = len(grid), len(grid[0])

        def dfs(r,c):

            if min(r,c) < 0 or r >= ROW or c >= COL or (r,c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r,c))
            
            count = 1+ dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

            return count
        
        maxIsland = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1 and (i,j) not in visit:
                    currIsland = dfs(i,j)
                    if maxIsland < currIsland:
                        maxIsland = currIsland
        
        return maxIsland






        