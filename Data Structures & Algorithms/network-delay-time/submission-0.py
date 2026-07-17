class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((t,v))
        
        min_heap = [(0,k)]
        res = 0
        visited = set()
        while min_heap:
            time,node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            # res+=time
            res= max(res,time)
            for t,e in adj[node]:
                if e not in visited:
                    heapq.heappush(min_heap,(time+t,e))
                    # q.append((e,t))
        print(len(visited))
        if len(visited)!=n:
            return -1
        else:
            return res


