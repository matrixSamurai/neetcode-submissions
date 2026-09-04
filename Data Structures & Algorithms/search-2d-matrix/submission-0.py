class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        startCol = 0
        endCol = len(matrix[0]) -1 
        ansCol = -1


        startRow = 0
        endRow = len(matrix) - 1
        ansRow = -1

        rowLength = len(matrix[0])

        while startRow <= endRow:
            
            midRow = (startRow + endRow ) //2

            print(f"Row is : {midRow}")
            print(f"{matrix[midRow][0]} : {target} : {matrix[midRow][rowLength - 1]}")

            if matrix[midRow][0]  <= target <= matrix[midRow][rowLength - 1]:
                ansRow = midRow
                break
            elif matrix[midRow][0]  > target:
                endRow = midRow - 1
            else:
                startRow = midRow + 1
            
            print(f"Last are {startRow} : {endRow} : {ansRow}")
        
        print(f"THe answer row is {ansRow}")
        
        while startCol <= endCol:
            
            print(f"Start col and endCol is : {startCol} : {endCol}")

            midCol = (startCol + endCol ) //2

            print(f"Col is : {midCol}")

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
        


        