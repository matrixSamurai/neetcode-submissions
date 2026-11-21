class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ## First to do the bianry search to select the row

        ROW, COL = len(matrix), len(matrix[0])

        topRow = 0
        bottomRow = ROW -1

        while topRow <= bottomRow:
            
            midRow = (bottomRow + topRow) // 2

            if matrix[midRow][COL-1] < target:
                topRow = midRow + 1
            elif matrix[midRow][0] > target:
                bottomRow = midRow - 1
            else:
                break
        
        ## Now we have the correct Row

        leftCol = 0
        rightCol = COL -1

        while leftCol <= rightCol:
            
            midCol = (leftCol + rightCol) // 2

            if matrix[midRow][midCol] < target:
                leftCol = midCol + 1
            elif matrix[midRow][midCol] > target:
                rightCol = midCol - 1
            else:
                return True
        
        return False





        