class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        maxTime = 0

        def bfs():

            nonlocal maxTime

            neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
            level = 0
            
            while queue:

                level += 1
                
                queueLen = len(queue)
            
                for i in range(queueLen):

                    x,y = queue.popleft()

                    for dx, dy in neighbors:

                        dr, dc = x + dx, y+dy

                        if min(dr, dc) < 0 or dr >= ROW or dc >= COL or grid[dr][dc] == 0:
                            continue
                        
                        if (dr,dc) not in visit:
                            grid[dr][dc] = 2
                            visit.add((dr,dc))
                            queue.append((dr,dc))

                            if  maxTime < level:
                                maxTime = level


        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==2:
                    visit.add((i,j))
                    queue.append((i,j))
        
        bfs()

        print(grid)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1

        if maxTime == float("-inf"):
            return -1
        
        return maxTime
        