class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q= deque()
        def addCell(r,c):
            if r<0 or r>= ROWS or c<0 or c>=COLS:
                return
            if (r,c) in visited or grid[r][c]==0:
                return
            q.append((r,c))
            visited.add((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                    visited.add((r,c))
        time=-1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=2
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            time+=1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    return -1
        
        return max(time,0)

