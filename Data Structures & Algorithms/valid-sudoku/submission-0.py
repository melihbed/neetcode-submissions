class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}

        # check each row
        for row in board:
            for num in row:
                if num == ".":
                    continue
                if num not in hashmap:
                    hashmap[num] = 1
                else: 
                    return False 
            
            hashmap.clear()
        hashmap.clear()
        # check each column
        for col in zip(*board):
            for num in col:
                if num == ".":
                    continue
                if num not in hashmap:
                    hashmap[num] = 1
                else: 
                    return False
            hashmap.clear()
        hashmap.clear()

        # check each sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                # go inside one 3x3 box
                for i in range(3):
                    for j in range(3):
                        if board[box_row + i][box_col + j] == ".":
                            continue
                        if board[box_row + i][box_col + j] not in hashmap:
                            hashmap[board[box_row + i][box_col + j]] = 1
                        else:
                            return False
                hashmap.clear()
        return True


