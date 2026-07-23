class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProf = 0
        dp = defaultdict(int)
        def dfs(i,holding):
            if i>=len(prices):
                return 0
            if (i,holding) in dp:
                return dp[(i,holding)]
            if holding:
                #sell
                res = max(prices[i] + dfs(i+2,0),dfs(i+1,1))
            else:
                res = max(-prices[i]+dfs(i+1,1),dfs(i+1,0))
            dp[(i,holding)]=res
            return res
                    
        # dfs(0,0)
        return dfs(0,0)