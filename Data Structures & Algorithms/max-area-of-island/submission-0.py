class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i,j,grid):

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
        
            if grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i+1,j,grid) + dfs(i,j+1,grid) + dfs(i-1,j,grid) + dfs(i,j-1,grid)
            else:
                return 0
        

        maxArea = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    localMax = dfs(i,j,grid)
                    if localMax > maxArea:
                        maxArea = localMax
                        print(maxArea)

        return maxArea


        