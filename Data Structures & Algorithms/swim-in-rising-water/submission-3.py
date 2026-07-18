class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        min_heap = [(grid[0][0], 0, 0)]
        visited = set()

        directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]

        while min_heap:
            elev, x, y = heapq.heappop(min_heap)

            if (x, y) in visited:
                continue

            visited.add((x, y))

            if x == rows - 1 and y == cols - 1:
                return elev

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and (nx, ny) not in visited
                ):
                    heapq.heappush(
                        min_heap,
                        (max(elev, grid[nx][ny]), nx, ny)
                    )