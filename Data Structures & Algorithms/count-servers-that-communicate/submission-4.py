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

from typing import List
from collections import defaultdict


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        row_servers = defaultdict(list)
        col_servers = defaultdict(list)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_servers[r].append((r, c))
                    col_servers[c].append((r, c))

        visited = set()
        processed_rows = set()
        processed_cols = set()
        answer = 0

        for start_row in row_servers:
            for start in row_servers[start_row]:
                if start in visited:
                    continue

                stack = [start]
                visited.add(start)
                component_size = 0

                while stack:
                    r, c = stack.pop()
                    component_size += 1

                    # Process this entire row only once
                    if r not in processed_rows:
                        processed_rows.add(r)

                        for neighbor in row_servers[r]:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                stack.append(neighbor)

                    # Process this entire column only once
                    if c not in processed_cols:
                        processed_cols.add(c)

                        for neighbor in col_servers[c]:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                stack.append(neighbor)

                if component_size > 1:
                    answer += component_size

        return answer




        



