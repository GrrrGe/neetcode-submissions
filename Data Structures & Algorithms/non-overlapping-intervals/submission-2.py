class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        res = [[float('-inf'),float('-inf')]]
        count = 0
        print(intervals)
        for start,end in intervals:
            lastEnd = res[-1][1]
            if lastEnd>start:
                count+=1
                # res[-1][1]=min(res[-1][1],end)
            else:
                res.append([start,end])
        print(res)
        return count