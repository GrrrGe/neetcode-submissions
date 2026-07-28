class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix),len(matrix[0])
        matrix.reverse()
        for i in range(ROWS):
            for j in range(i+1,COLS):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]