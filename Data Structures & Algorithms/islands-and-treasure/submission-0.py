class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        land = 2**31 -1
        ROW, COL = len(grid), len(grid[0])

        ## Iterative in nature
        def bfs(r,c):

            queue = deque()
            visit = set()

            visit.add((r,c))
            queue.append((r,c))

            neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

            level = 0

            while queue:

                level+= 1
                numberOfNodes = len(queue)
           
                for i in range(numberOfNodes):

                    x, y = queue.popleft()


                    for dx,dy in neighbors:
                        dr, dc = x + dx, y+dy

                        if min(dr,dc) < 0 or dr >= ROW or dc >= COL or grid[dr][dc] == -1:
                            continue
                    
                        if grid[dr][dc] >= level:
                            grid[dr][dc]= level
                            if (dr,dc) not in visit:
                                visit.add((dr,dc))
                                queue.append((dr,dc))
                    

        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==0:
                    bfs(i,j)


