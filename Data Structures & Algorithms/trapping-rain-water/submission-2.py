class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0]*n, [0]*n
        if n == 0:
            return 0
        left[0] = height[0]
        right[n-1] = height[n-1]
        for i in range(1,n):
            left[i] = max(left[i-1],height[i])
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        area = 0
        for i in range(n):
            cur = min(left[i],right[i])-height[i]
            if cur:
                area+=cur
        return area



