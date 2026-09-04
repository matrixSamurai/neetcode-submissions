class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Creating the map of the sets here, and using the defaultdict 
        # So that if the key is not present, create one with the empty val
        hashmapRowSet = defaultdict(set)
        hashmapColSet = defaultdict(set)
        hashmapBoxSet = defaultdict(set)

        for rowIndex, row in enumerate(board):
            for colIndex, element in enumerate(row):
                if element != ".":

                    if element in hashmapRowSet[rowIndex]:
                        return False
                    else:
                        hashmapRowSet[rowIndex].add(element)

                    if element in hashmapColSet[colIndex]:
                        return False
                    else:
                        hashmapColSet[colIndex].add(element)

                    boxIndex = (int(rowIndex/3), int(colIndex/3))

                    if element in hashmapBoxSet[boxIndex]:
                        return False
                    else:
                        hashmapBoxSet[boxIndex].add(element)
        

        return True





        