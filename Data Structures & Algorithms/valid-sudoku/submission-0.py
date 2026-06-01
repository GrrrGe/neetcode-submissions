class Solution:
    def checkRows(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [0]*10
            for j in range(9):
                if(board[i][j]!="."):
                    row[int(board[i][j])]+=1
            for j in range(1,10):
                if row[j]>1:
                    return False
        return True
                
    def checkColumns(self, board: List[List[str]]) -> bool:
        for i in range(9):
            col = [0]*10
            for j in range(9):
                if(board[j][i]!="."):
                    col[int(board[j][i])]+=1
            for j in range(1,10):
                if col[j]>1:
                    return False
        return True
    
    def checkSubBoxes(self, board: List[List[str]]) -> bool:
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                subBox = [0]*10
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        if(board[i+k][j+l]!="."):
                            subBox[int(board[i+k][j+l])]+=1
                for val in range(1,10):
                    if subBox[val] > 1:
                        return False
        return True
                


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkColumns(board) and self.checkSubBoxes(board)