class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=dp[1]=1
        for r in range(2,n+1):
            dp[r]=dp[r-1]+dp[r-2]
        return dp[n]
        