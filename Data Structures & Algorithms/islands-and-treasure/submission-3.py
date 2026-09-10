## THe trick is to do the level by level traversal from all the 0 blocks
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROW, COL = len(grid), len(grid[0])

        queue = deque()
        visit = set()

        ## Iterative in nature
        def bfs():

            neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

            level = 0

            while queue:

                level+= 1
                numberOfNodes = len(queue)
           
                for i in range(numberOfNodes):

                    x, y = queue.popleft()


                    for dx,dy in neighbors:
                        dr, dc = x + dx, y+dy

                        if min(dr,dc) < 0 or dr >= ROW or dc >= COL or grid[dr][dc] == -1 or grid[dr][dc] == 0:
                            continue
                    
                        if grid[dr][dc] > level:
                            grid[dr][dc]= level
                            if (dr,dc) not in visit:
                                visit.add((dr,dc))
                                queue.append((dr,dc))
                    

        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==0:
                    visit.add((i,j))
                    queue.append((i,j))

        bfs()


