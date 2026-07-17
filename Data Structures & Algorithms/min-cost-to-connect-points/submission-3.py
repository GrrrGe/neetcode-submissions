class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        visited = set()
        min_heap = [(0,points[0])]
        res = 0
        while min_heap:
            dist,(x,y)=heapq.heappop(min_heap)
            if (x,y) in visited:
                continue
            res+=dist
            visited.add((x,y))
            for x2,y2 in points:
                if x == x2 and y == y2:
                    continue
                if (x2,y2) in visited:
                    continue
                curr = abs(x-x2) + abs(y-y2)
                heapq.heappush(min_heap,(curr,(x2,y2)))

        
        return res



