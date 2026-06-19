class MedianFinder:

    def __init__(self):
        self.minHeap = [] #big
        self.maxHeap = [] # small

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.maxHeap,num)
        if self.minHeap and self.maxHeap[0]>self.minHeap[0]:
            heapq.heappush(self.minHeap,heapq.heappop_max(self.maxHeap))
        if len(self.minHeap) + 1 <len(self.maxHeap):
            heapq.heappush(self.minHeap,heapq.heappop_max(self.maxHeap))
        if len(self.minHeap)>len(self.maxHeap):
            heapq.heappush_max(self.maxHeap,heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        # if len(self.maxHeap)==0:
        #     return self.minHeap[0]
        if len(self.minHeap)<len(self.maxHeap):
            return self.maxHeap[0]
        return (self.minHeap[0]+self.maxHeap[0])/2
        
        