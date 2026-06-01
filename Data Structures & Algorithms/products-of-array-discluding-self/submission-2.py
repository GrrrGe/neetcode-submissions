class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suff = 1, 1
        ans = []
        for num in nums:
            ans.append(pref)
            pref = pref * num
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i]* suff
            suff = suff * nums[i]
        return ans
        #1 2 3 6
        