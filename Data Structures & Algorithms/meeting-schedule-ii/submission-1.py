"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        intervals.sort(key = lambda i:i.start)
        res = [[intervals[0]]]
        for interval in intervals[1:]:
            flag = False
            for intervals in res:
                if intervals[-1].end<=interval.start:
                    intervals.append(interval)
                    flag =True
                    break
            if not flag:
                res.append([interval])
        return len(res)
        