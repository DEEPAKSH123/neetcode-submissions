"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        i=intervals[0]
        prevend=i.end
        for i in range(1,len(intervals)):
            val=intervals[i]
            if val.start<prevend:
                return False
            else:
                prevend=max(val.end,prevend)
        return True
