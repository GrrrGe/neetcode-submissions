class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            if nums[abs(nums[i])-1]<0:
                return abs(n)
            else:
                nums[abs(nums[i])-1]*=-1
        return