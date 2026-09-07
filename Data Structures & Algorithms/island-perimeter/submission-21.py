## Simply Traversing all the nodes of the m*n matrix and checking how many neighbors each node have. Ans = summation over node (4 - neighbors)
# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:

#         perimeter = 0

#         for i in range(len(grid)):
#             for j in range(len(grid[0])):

#                 if grid[i][j] == 1:
#                     perimeter += 4
                
#                     if i-1 >= 0 and grid[i-1][j] == 1:
#                         perimeter -= 1
#                     if i+1 < len(grid) and grid[i+1][j] == 1:
#                         perimeter -= 1
#                     if j-1 >= 0 and grid[i][j-1] == 1:
#                         perimeter -= 1
#                     if j+1 < len(grid[0]) and grid[i][j+1] == 1:
#                         perimeter -= 1

#         return perimeter



## DFS solutions
## Using the DFS as the travelling engine - the logic is -:
# When you hit the boundary or the 0neightbor, return 1, becuase
# that represents the edge of the perimeter

# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:

#         visit = set()
#         ROW, COL = len(grid), len(grid[0])

#         def dfs(r,c):
#             if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] == 0:
#                 return 1
            
#             if (r,c) in visit:
#                 return 0
            
            
#             visit.add((r,c))
#             return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)


#         for i in range(ROW):
#             for j in range(COL):
#                 if grid[i][j] == 1:
#                    return dfs(i,j)
        

## BFS solutions
## Using the BFS as the travelling engine - the logic is -:
# When you hit the boundary or the 0 neightbor, return 1, becuase
# that represents the edge of the perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        queue = deque()
        visit = set()
        ROW, COL = len(grid), len(grid[0])
        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]


        def bfs(r,c):

            queue.append((r,c))
            perim = 0

            while queue:

                x,y = queue.popleft()
                
                for dx, dy in neighbors:
                    tr = x + dx
                    tc = y + dy

                    if min(tr,tc) < 0 or tr == ROW or tc == COL or grid[tr][tc] == 0:
                        perim += 1
                    elif (tr,tc) not in visit:
                        visit.add((tr,tc))
                        queue.append((tr,tc))
            
            return perim
                    

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    visit.add((i,j))
                    return bfs(i,j)





        