"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda c: c.start)
        res=[]
        if intervals==[]:
            return True
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            
            e=res[-1]
            print(res)
            if intervals[i].start<e.end:
                return False
            else:
                res.append(intervals[i])
                print(res)

        return True
