class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        rightMax = [0]*n
        leftMax = [0]*n
        leftMax[0]=height[0]
        rightMax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],height[i])
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1],height[i])
        rain = 0
        for i in range(1,n-1):
            curr = min(leftMax[i-1],rightMax[i+1])-height[i]
            rain+= curr if curr>0 else 0

        return rain


