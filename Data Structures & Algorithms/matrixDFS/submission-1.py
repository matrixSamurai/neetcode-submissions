class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        visited = set()

        def dfs(grid, row, col, visited):

            rowMax, colMax = len(grid), len(grid[0])

            if row < 0 or col < 0 or row == rowMax or col == colMax:
                return 0

            if (row, col) in visited or  grid[row][col] == 1:
                return 0
           
            if row == rowMax -1 and col == colMax -1:
                return 1 
            
            visited.add((row, col))

            count = 0

            count += dfs(grid, row + 1, col, visited) 
            count += dfs(grid, row, col+1, visited) 
            count += dfs(grid, row - 1, col, visited) 
            count += dfs(grid, row, col - 1, visited) 

            # THis is the crucial step for the backtracking where         #remove the nodes added to the visited to allow for the new and different 
            #paths but with some of the nodes same
            visited.remove((row, col))
            return count
        
        return dfs(grid, 0,0,visited)



        