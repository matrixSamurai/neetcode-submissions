class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        visited = set()
        ROW, COL = len(grid), len(grid[0])
        r,c = -1, -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    r,c = i,j
                    break
            if r != -1:
                break        

        stack = []
        stack.append((r,c))
        perimeter = 0
        visited.add((r,c))

        while stack:

            node = stack.pop()
            perimeter += 4

            neighbors = [(node[0]+1, node[1]), (node[0]-1, node[1]),
            (node[0], node[1]+1), (node[0], node[1]-1)]

            for dr, dc in neighbors:

                if min(dr,dc) < 0 or dr == ROW or dc == COL:
                    continue
                
                if grid[dr][dc] == 1:
                    perimeter -= 1
                    if (dr,dc) not in visited:
                        stack.append((dr,dc))
                        visited.add((dr,dc))
                        
            
            print(node)
            print(stack)
            print(visited)

            print(perimeter)
            print("*******")


        

        return perimeter






            
            

            
            
        

        