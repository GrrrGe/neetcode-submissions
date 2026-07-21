class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp= [-1]*(amount+1)
        dp[0] = 0
        def dfs(amount):
            if dp[amount]!=-1:
                return dp[amount]
            if amount == 0:
                return 0

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    if dp[amount - coin]!=-1:
                        res = min(res,1+ dp[amount - coin])
                    else:
                        res = min(res, 1 + dfs(amount - coin))
            dp[amount] = res
            return dp[amount]

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
