class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMaxes, rightMaxes = [0]*n, [0]*n
        lmax ,rmax = 0,0
        for i in range(n):
            lmax = max(lmax, height[i])
            leftMaxes[i] = lmax
        
        for j in range(n-1,-1,-1):
            rmax = max(rmax, height[j])
            rightMaxes[j] = rmax
        total_area = 0
        for i in range(n):
            total_area += min(leftMaxes[i], rightMaxes[i]) -  height[i] 
        return total_area
            
        
