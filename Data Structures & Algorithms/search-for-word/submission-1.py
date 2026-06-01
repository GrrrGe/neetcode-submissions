class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board and word:
            return False
        if not board and not word:
            return True
        flag = False
        def dfs(i,j,cur):
            if cur == len(word):
                nonlocal flag 
                flag = True
                return
            if i >= len(board) or j >= len(board[0]):
                return
            if i< 0 or j< 0:
                return

            if(word[cur] == board[i][j]):
                temp = board[i][j]
                board[i][j] = "*"
                dfs(i+1,j,cur+1)
                dfs(i-1,j,cur+1)
                dfs(i,j+1,cur+1)
                dfs(i,j-1,cur+1)
                board[i][j] = temp
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                dfs(i,j,0)
        return flag


            

        