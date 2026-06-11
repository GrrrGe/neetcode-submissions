class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        l,r = 0,0
        if k==1:
            return nums
        while r<k:
            heapq.heappush(heap, (-nums[r],r))
            r+=1
        
        ans = []
        ans.append(-heap[0][0])
        l+=1
        while r<len(nums):
            heapq.heappush(heap,(-nums[r],r))
            while heap[0][1] < l:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
            l+=1
            r+=1
        return ans

