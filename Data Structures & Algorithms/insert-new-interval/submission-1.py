class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            x,y = intervals[i]
            if newInterval[1]<x:
                return res+[newInterval]+intervals[i:]
            if newInterval[0]>y:
                res.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],x),max(newInterval[1],y)]
        return res+[newInterval]
