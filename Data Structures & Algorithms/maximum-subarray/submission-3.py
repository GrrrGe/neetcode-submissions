class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ans = -float('inf')
        dp = [*nums]
        def dfs(i):
            # if (i,curSum) in dp:
            #     return 
            # nonlocal ans
            # ans = max(ans,curSum)
            if i==len(nums):
                return
            
            
            dp[i] = max(dp[i],dp[i-1]+nums[i])
            dfs(i+1)

            return
        
        dfs(1)
        return max(dp)
        