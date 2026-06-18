class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums =[]
        for n in nums1:
            nums.append(n)
        for n in nums2:
            nums.append(n)
        
        nums.sort()
        n = len(nums)
        if n%2==0:
            n1,n2= nums[n//2],nums[(n-1)//2]
            return (n1+n2)/2
        else:
            return nums[n//2]