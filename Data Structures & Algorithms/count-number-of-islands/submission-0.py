class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r,c):

            if grid[r][c] == '1':
                grid[r][c] = '0'

                if r > 0:
                    dfs(r-1,c)
                if r < len(grid) - 1:
                    dfs(r+1,c)
                if c > 0:
                    dfs(r,c-1)
                if c < len(grid[0]) -1:
                    dfs(r,c+1)

        islands = 0
        # print(len(grid))
        # print(len(grid[0]))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        
        return islands

       
            

    



        