class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS,COLS = len(grid), len(grid[0])
        # matrix = [[float('inf') for i in range(COLS)]*ROWS]
        min_heap = [(grid[0][0],0,0)]
        dirs = [(0,-1),(-1,0),(1,0),(0,1)]
        visited = set()
        while min_heap:
            elev, x, y = heapq.heappop(min_heap)
            if x < 0 or x>= ROWS or y<0 or y>=COLS or (x,y) in visited:
                continue
            if x== ROWS-1 and y==COLS-1:
                return max(elev,grid[x][y])
            visited.add((x,y))
            grid[x][y] = max(elev,grid[x][y])
            heapq.heappush(min_heap,(grid[x][y],x+1,y))
            heapq.heappush(min_heap,(grid[x][y],x,y+1))
            heapq.heappush(min_heap,(grid[x][y],x-1,y))
            heapq.heappush(min_heap,(grid[x][y],x,y-1))

        return