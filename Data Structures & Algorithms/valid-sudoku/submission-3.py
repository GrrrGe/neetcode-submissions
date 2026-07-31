class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9,9
        ROW = [set()for i in range(9)]
        COL = [set()for i in range(9)]
        SUB = [[set() for i in range(3)] for i in range(3)]

        for i in range(ROWS):
            for j in range(COLS):
                node = board[i][j]
                if node =='.':
                    continue
                if node not in ROW[i] and node not in COL[j] and node not in SUB[i//3][j//3]:
                    print([i,j])
                    print("Adding node")
                    print(node)
                    ROW[i].add(node)
                    COL[j].add(node)
                    SUB[i//3][j//3].add(node)
                else:
                    print([i,j])
                    return False
        return True
