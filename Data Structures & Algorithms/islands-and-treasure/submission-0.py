class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid),len(grid[0])
        
        def dfs(r,c,path):
            if r < 0 or r>=ROWS or c<0 or c>=COLS:
                return
            
            if grid[r][c]==-1 or grid[r][c]<path:
                return
            grid[r][c]=path
            dfs(r+1,c,path+1)
            dfs(r-1,c,path+1)
            dfs(r,c+1,path+1)
            dfs(r,c-1,path+1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    dfs(r,c,0)
        
            
            