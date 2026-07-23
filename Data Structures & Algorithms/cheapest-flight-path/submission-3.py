class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adj = defaultdict(list)
        # for src,des,cost in flights:
        #     adj[src].append([cost,des])
        prices = [float('inf')]*n
        prices[src]=0
        for i in range(k+1):
            temp = prices.copy()
            for src,des,p in flights:
                if prices[src] == float('inf'):
                    continue
                if prices[src]+p < temp[des]:
                    temp[des]=prices[src]+p
            prices=temp
        
        return -1 if prices[dst]==float('inf') else prices[dst]

