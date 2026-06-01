class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(i,j,curr):
            if curr == len(word):
                return True
            if i < 0 or j < 0 or i >= ROWS or j>= COLS:
                return
            if board[i][j]!=word[curr]:
                return
            board[i][j]="*"
            res = (dfs(i+1,j,curr+1) or
                dfs(i-1,j,curr+1) or
                dfs(i,j+1,curr+1) or
                dfs(i,j-1,curr+1))
            board[i][j] = word[curr]
            return res
        for i in range(0,ROWS):
            for j in range(0,COLS):
                if dfs(i,j,0):
                    return True
        return False