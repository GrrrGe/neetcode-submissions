class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_count = 0
        if(len(nums)==0):
            return 0
        curr_count = 1
        for i in range(1,len(nums)):
            # print(nums[i])
            if nums[i-1]+1 == nums[i]:
                curr_count+=1
            elif nums[i-1] != nums[i]:
                max_count = max(max_count, curr_count)
                curr_count = 1
        
        return max(max_count,curr_count)