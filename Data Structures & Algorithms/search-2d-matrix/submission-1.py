class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        startCol = 0
        endCol = len(matrix[0]) -1 
        ansCol = -1


        startRow = 0
        endRow = len(matrix) - 1
        ansRow = -1

        rowLength = len(matrix[0])

        # This is the vertical search, to find the perfect row for the binary search to continue
        while startRow <= endRow:
            
            midRow = (startRow + endRow ) //2
            
            if matrix[midRow][0]  <= target <= matrix[midRow][rowLength - 1]:
                ansRow = midRow
                break
            elif matrix[midRow][0]  > target:
                endRow = midRow - 1
            else:
                startRow = midRow + 1
            
        
        # STart the searching in the row now, actual binary search of the row
        while startCol <= endCol:
            
            midCol = (startCol + endCol ) //2

            if matrix[ansRow][midCol]  == target:
                ansCol = midCol
                break
            elif matrix[ansRow][midCol]  > target:
                endCol = midCol - 1
            else:
                startCol = midCol + 1


        if ansRow != -1 and ansCol != -1:
            return True
        else:
            return False
        


        