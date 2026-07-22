class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # curr = [nums[0]]
        n = len(nums)
        memo = [-1]*n

        def dfs(i):
            if memo[i]!=-1:
                return memo[i]
            memo[i]=1
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    memo[i]=max(memo[i],1+dfs(j))
            return memo[i]
        # for i in range(n):
        #     dfs(i)
        return max(dfs(i) for i in range(n))
