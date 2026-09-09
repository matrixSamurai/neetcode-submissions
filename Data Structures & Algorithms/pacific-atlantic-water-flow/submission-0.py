## This is the tricky problem - which you should remember
## First of all, you should start traversing (DFS)from the opposite, from the edges of the Pacific and the atlantic. Now you maintain the set of the cells which are 
#reachable by the pacific, and then also other set reachable from the atlantic. 
# Now, the answer is the cells which are reachable by both of them.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacificCells = set()
        atlanticCells = set()

        ROW, COL = len(heights), len(heights[0])


        def dfs(r,c, reachable):
           
            if (r,c) in reachable:
                return

            stack = []
            neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
            stack.append((r,c))

            if (r,c) not in reachable:
                reachable.add((r,c))
            
            while stack:

                x, y = stack.pop()
                for dx, dy in neighbors:
                    dr, dc = x+dx, y+dy
                    if min(dr,dc) < 0 or dr == ROW or dc == COL or heights[dr][dc] < heights[x][y]:
                        continue
                    
                    if (dr,dc) not in reachable:
                        reachable.add((dr,dc))
                        stack.append((dr,dc))

        
        for i in range(COL):
            dfs(0,i, pacificCells)
            dfs(ROW-1, i, atlanticCells)
        for j in range(ROW):
            dfs(j,0, pacificCells)
            dfs(j, COL-1, atlanticCells)

        answer = []

        print(pacificCells)
        print("********")
        print(atlanticCells)
        
        for item in pacificCells:
            if item in atlanticCells:
                answer.append([item[0], item[1]])
        
        return answer
        


     