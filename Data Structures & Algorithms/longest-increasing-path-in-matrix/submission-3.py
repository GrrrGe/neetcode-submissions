class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        # visited = set()
        # dr = [[0,1],[0,-1],[1,0],[-1,0]]
        dr = ((1,0),(-1,0),(0,1),(0,-1))
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            # if i<0 or i>=ROWS or j<0 or j>=COLS or (i,j) in visited:
            #     return 0
            # visited.add((i,j))
            res =1
            for dx,dy in dr:
                nr,nc = i+dx, j+dy
                if nr<0 or nr >=ROWS or nc<0 or nc>=COLS:
                    continue
                if matrix[nr][nc]>matrix[i][j]:
                    res=max(res,1+dfs(nr,nc))
            # visited.remove((i,j))
            dp[(i,j)]= res
            return dp[(i,j)]
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j)
        return max(dp.values())
            