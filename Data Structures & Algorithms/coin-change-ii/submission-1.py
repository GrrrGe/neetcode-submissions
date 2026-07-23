class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i,amount):
            if (i,amount) in dp:
                return dp[(i,amount)]

            if amount == 0 :
                return 1
            if i==len(coins) or amount<0:
                return 0
            dp[(i,amount)] = dfs(i,amount-coins[i])+ dfs(i+1,amount)
            return dp[(i,amount)]
            
           
            # return 
        return dfs(0,amount)