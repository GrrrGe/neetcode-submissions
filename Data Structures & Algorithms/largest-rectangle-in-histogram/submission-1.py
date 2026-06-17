class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                start, height = stack.pop()
                area = height* (i-start)
                maxArea = max(maxArea,area)
            
            stack.append([start,h])
        
        while len(stack):
            start, height = stack.pop()
            area = height* (len(heights)-start)
            maxArea = max(maxArea,area)

        return maxArea
