class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        return max(self.rob2(nums[0:n-1]),self.rob2(nums[1:n]))
    
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n>1:
            nums[1]=max(nums[0],nums[1])
        for i in range(2,n):
            nums[i]=max(nums[i-1],nums[i-2]+nums[i])
        
        return nums[n-1]