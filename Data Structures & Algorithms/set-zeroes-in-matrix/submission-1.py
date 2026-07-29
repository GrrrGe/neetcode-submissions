class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS,COLS = len(matrix),len(matrix[0])
        # row = set()
        # col = set()
        top_row = False
        left_col = False
        for i in range(ROWS):
            if matrix[i][0]==0:
                left_col = True
                break
        for j in range(COLS):
            if matrix[0][j]==0:
                top_row = True
                break
    
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if matrix[0][j]==0:
                    matrix[i][j]=0
                elif matrix[i][0]==0:
                    matrix[i][j]=0
        for i in range(ROWS):
            if left_col:
                matrix[i][0]=0
        for j in range(COLS):
            if top_row:
                matrix[0][j]=0
