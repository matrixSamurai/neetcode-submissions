class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])

        visited = {(0,0)}

        queue = deque()

        ## The last 0 is the position of the current element from start
        if grid[0][0] == 0:
            queue.append((0,0,0))
        else:
            return -1


        path = 0

        while queue:

            r,c,l = queue.popleft()

            if r == ROW-1 and c == COL -1:
                return l

            neighbors = [[1,0],[0,1],[-1,0],[0,-1]]

            for dr, dc in neighbors:
                if min(r+dr, c+dc) < 0 or r+dr == ROW or c + dc == COL or grid[r+dr][c+dc] == 1 or (r+dr, c+dc) in                visited:
                 
                    continue
                
                queue.append((r+dr, c+dc, l+1))
                visited.add((r+dr, c+dc))
            
        return -1


            
        