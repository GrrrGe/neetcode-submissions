class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        for v in count.values():
            heap.append(v)
        
        heapq.heapify_max(heap)
        idle = deque()
        time = 0
        while heap or idle:
            time +=1
            if heap:
                v = heapq.heappop_max(heap)
                v-=1
                if v>0:
                    idle.append((time+n,v))
            if idle and idle[0][0]==time:
                v = idle.popleft()[1]
                heapq.heappush_max(heap,v)
    
        return time

