class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROW, COL = len(board), len(board[0])
        boundRegionSet = set()

        def dfs(r,c):

            if min(r,c) < 0 or r == ROW or c == COL or board[r][c] == "X" or (r,c) in boundRegionSet:
                return

            if board[r][c] == "O":
                boundRegionSet.add((r,c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for i in range(COL):
            dfs(0,i)
            dfs(ROW-1, i)
        
        for i in range(ROW):
            dfs(i,0)
            dfs(i, COL-1)

        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in boundRegionSet:
                    board[i][j]= "X"


        