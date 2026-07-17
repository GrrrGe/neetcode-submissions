class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tic = defaultdict(list)
        for s,d in tickets:
            tic[s].append(d)
        
        for s in tic:
            tic[s].sort(reverse=True)
        res = []
        def dfs(src):
            # if len(res) == len(tic):
            #     return
            while tic[src]:
                dfs(tic[src].pop())
            res.append(src)
        
        dfs("JFK")
        return res[::-1]
            

