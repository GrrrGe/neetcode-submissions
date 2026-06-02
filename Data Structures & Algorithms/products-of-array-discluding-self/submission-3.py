class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suf = 1, 1
        ans = []
        for n in nums:
            ans.append(pref)
            pref = pref*n
        for i in range(len(nums)-1,-1,-1):
            ans[i]=ans[i]*suf
            suf = suf*nums[i]
        return ans