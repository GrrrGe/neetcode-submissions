class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(i,j):
            if i< 0 or j<0 or i>= ROWS or j >= COLS:
                return
            if grid[i][j]=='1':
                grid[i][j] = 0
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        for i in range(0,ROWS):
            for j in range(0,COLS):
                if(grid[i][j]=='1'):
                    count+=1
                    dfs(i,j)
        return count
                
