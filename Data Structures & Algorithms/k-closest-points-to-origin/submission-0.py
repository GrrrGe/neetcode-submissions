class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            heapq.heappush(heap,(-dist,p))
        
        while len(heap)>k:
            heapq.heappop(heap)
        
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans