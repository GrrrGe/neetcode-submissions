class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        def dfs(i,count):
            if count == n:
                ans_board = []
                for i in range(len(board)):
                    ans_board.append("".join(board[i]))
                res.append(ans_board)
            if i>=n:
                return
            for j in range(n):
                board[i][j]='Q'
                if self.isValid(board,i,j,n):
                    dfs(i+1,count+1)
                board[i][j]='.'
        dfs(0,0)
        return res
    
    def isValid(self,board,i,j,n):
        for x in range(n):
            if x != j and board[i][x]=='Q':
                return False
            if x != i and board[x][j]=='Q':
                return False
        k,l = i-1, j-1
        while k>=0 and l>=0:
            if board[k][l]=='Q':
                return False
            k-=1
            l-=1
        k,l = i-1, j+1
        while k>=0 and l<n:
            
            if board[k][l]=='Q':
                return False
            k-=1
            l+=1
        k,l = i+1, j-1
        while k<n and l>=0:
            
            if board[k][l]=='Q':
                return False
            k+=1
            l-=1
        k,l = i+1, j+1
        while k<n and l<n:
            if board[k][l]=='Q':
                return False
            k+=1
            l+=1
        return True
