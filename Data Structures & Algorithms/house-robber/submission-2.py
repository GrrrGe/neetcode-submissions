class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        dp[len(nums)] = 0
        dp[len(nums)+1] = 0
        for i in range(len(nums)-1,-1,-1):
            if i in dp:
                return dp[i]
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])
            # return dp[i]
        return dp[0]
