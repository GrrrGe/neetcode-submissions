class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        
        flag = False

        def dfs(i,j,ind):
            if ind == len(word):
                nonlocal flag
                flag = True
                return 
            if i< 0 or i>=len(board) or j<0 or j>=len(board[0]):
                return
            
            if word[ind]!=board[i][j]:
                return
            # print("i: "+ str(i)  + " j:"+str(j) + " board[i][j]:"+board[i][j]+" ind:"+str(ind))

            temp = board[i][j]
            board[i][j]='.'
            dfs(i+1,j,ind+1)
            dfs(i,j+1,ind+1)
            dfs(i-1,j,ind+1)
            dfs(i,j-1,ind+1)
            board[i][j]=temp
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    dfs(i,j,0)
        
        return flag
