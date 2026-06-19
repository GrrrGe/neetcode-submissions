class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for n in nums:
            heapq.heappush(self.heap,n)
        self.k = k
        # self.heap = heapq.heapify(nums)



    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
