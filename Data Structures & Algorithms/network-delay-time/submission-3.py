class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((t,v))
        
        dist = {node:float("inf") for node in range(1,n+1)}
        def dfs(node,t):
            if t>=dist[node]:
                return
            
            dist[node]=t
            for time,nei in adj[node]:
                dfs(nei,t+time)
        
        dfs(k,0)
        res = max(dist.values())
        return res if res<float("inf") else -1


