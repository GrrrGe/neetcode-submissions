class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = [False]*n
        ans[n-1]=True
        for i in range(n-2,-1,-1):
            for j in range(min(i+nums[i],n-1),i,-1):
                if ans[j]:
                    ans[i]= True
                    break
        return ans[0]