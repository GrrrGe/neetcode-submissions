class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted((queries[i],i) for i in range(len(queries)))
        min_heap = []
        output= [-1]*len(queries)
        for q in queries:
            for start,end in intervals:
                if start<=q[0]:
                    heapq.heappush(min_heap,(end-start+1,end))
            while min_heap and min_heap[0][1]<q[0]:
                heapq.heappop(min_heap)
            if min_heap:
                output[q[1]]=min_heap[0][0]
            else:
                output[q[1]]=-1
        return output
