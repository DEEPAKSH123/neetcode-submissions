"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        if not intervals:
            return True
        prevend=intervals[0].end
        for x in intervals[1:]:
            if x.start<prevend:
                return False
            else:
                prevend=x.end
        return True