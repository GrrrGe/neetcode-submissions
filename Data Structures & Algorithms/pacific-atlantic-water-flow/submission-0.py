class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        ROWS, COLS = len(heights),len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(prevH,i,j,ocean):
            if i<0 or i>= ROWS or j<0 or j>=COLS:
                return
            currH = heights[i][j]
            if (i,j) in ocean or currH< prevH:
                return
            if currH>=prevH:
                ocean.add((i,j))
            
            dfs(currH,i+1,j,ocean)
            dfs(currH,i-1,j,ocean)
            dfs(currH,i,j+1,ocean)
            dfs(currH,i,j-1,ocean)
        
        for r in range(ROWS):
            dfs(heights[r][0],r,0,pacific)
            dfs(heights[r][COLS-1],r,COLS-1,atlantic)
        
        for c in range(COLS):
            dfs(heights[0][c],0,c,pacific)
            dfs(heights[ROWS-1][c],ROWS-1,c,atlantic)

        
        common = pacific.intersection(atlantic)
        return [[r,c] for (r,c) in common]
    

            


        