class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxPro = nums[0]
        minPro = nums[0]
        for r in range(1,len(nums)):
            curr = nums[r]
            temp = maxPro
            maxPro = max(maxPro*curr,minPro*curr,curr)
            minPro = min(temp*curr,minPro*curr,curr)
            res = max(res,maxPro)
        return res
