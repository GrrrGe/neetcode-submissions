class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = max(heights)
        ans = 0
        area = 0
        for i in range(m+1):
            for h in heights:
                if h >=i:
                    area+=i
                    ans = max(ans,area)
                else:
                    area=0
            area = 0
        return ans
