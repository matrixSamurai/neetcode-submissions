## THe trick is to do the level by level traversal from all the 0 blocks

# TIme complexity is - O(m*n)^2
#Soltuion 1: The idea is to call the BFS from each of the Treasure chest and do the DFS from all of them in the standard way, but this is inefficient as there be many nodes which will be process many times

## BEST solution - O(m*n)
#Solution 2: The best approach is to initalise the quwue with all the treasure chest in the board, and start the parallel BFS from all of the them not just one node as compared to the standard DFS, that they we save too many same nodes to be processed. This is based on the idea that, the wave from which of the following treasure reaches first to the the land should have that answer as we are traversing level by level.

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


