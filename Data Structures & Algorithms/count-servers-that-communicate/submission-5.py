## This is the recursive DFS soltuion, the recursion doesn't work very well for the 
## large matrix, better to use the iterative DFS

# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:

#         connected = 0
#         visit = set()
#         ROW, COL = len(grid), len(grid[0])

#         def dfs(r, c, direction):

#             if min(r,c) < 0 or r == ROW or c == COL:
#                 return 0
            
#             if grid[r][c] == 0:
#                 return dfs(r + direction[0], c + direction[1], direction)
            
#             if grid[r][c] == 1 and (r,c) not in visit:
#                 visit.add((r,c))
#                 count = dfs(r+1, c, (1, 0)) + dfs(r-1, c, (-1, 0)) + dfs(r, c+1, (0, 1)) + dfs(r, c-1, (0, -1)) 

#                 if count > 0:
#                     count += 1
#                     return count
#                 elif count == 0 and direction == (0,0):
#                     return 0
#                 else:
#                     return 1
#             else:
#                 return 0


#         for i in range(ROW):
#             for j in range(COL):
#                 if grid[i][j] == 1 and (i,j) not in visit:
#                     connected += dfs(i,j,(0,0))
        
#         return connected

    
## Using the iterative DFS now to accompolish the traversal in the big matrix
## which is again hard to visualise, the simple soltution is just matrix travel

## Sol - COunt the no of server sin both the rows and the col and store them in array
## Now traverse the matrix again for each element and check if that elements row or 
## column, the count is more than 1, add that server to the answer


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        rowCount = [0] * len(grid)
        colCount = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        
        connected = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (rowCount[i] > 1 or colCount[j] > 1):
                    connected += 1
        
        return connected


