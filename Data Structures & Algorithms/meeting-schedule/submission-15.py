"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res=[]
        if not intervals:
            return True
        intervals.sort(key = lambda x:x.start)
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[-1].end >intervals[i].start:
                return False
            else:
                res.append(intervals[i])
        return True

