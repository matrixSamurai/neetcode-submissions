# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:

#         def dfs(i,j,grid):

#             ## Handling the out of bounds index here
#             if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
#                 return

#             if grid[i][j] == "1":
#                 grid[i][j] = 0
            
#             ## Running all the possible directions
#                 dfs(i+1, j, grid)
#                 dfs(i, j+1, grid)
#                 dfs(i-1, j, grid)
#                 dfs(i, j-1, grid)
            

#         numIslands = 0

#         for i in range(0, len(grid)):
#             for j in range(0, len(grid[0])):
#                 print(grid)
#                 if grid[i][j] == "1":
#                     numIslands += 1
#                     dfs(i,j,grid)
#                     print(i,j)
#                     print(grid)
        
#         return numIslands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visit = set()
        ROW, COL = len(grid), len(grid[0])

        def dfs(r,c):

            stack = []
            visit.add((r,c))
            stack.append((r,c))


            neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

            while stack:

                x, y = stack.pop()

                for dx, dy in neighbors:
                    dr = x + dx
                    dc = y + dy

                    if min(dr,dc) < 0 or dr >= ROW or dc >= COL or grid[dr][dc] == "0" or (dr,dc) in visit:
                        continue
                    
                    visit.add((dr,dc))
                    stack.append((dr,dc))
                    
    

        islands = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(i,j)
                    islands += 1
        
        return islands




        

       
            

    



        