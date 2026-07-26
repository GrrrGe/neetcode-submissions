class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = len(nums)-1
        count = 0
        while cur>0:
            for i in range(0,cur+1):
                if i+ nums[i]>=cur:
                    cur=i
                    count+=1
                    break
        return count
