"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        start={}
        end={}
        timeline=[]
        count=0
        ans=0
        for i in range(len(intervals)):
            start[intervals[i].start]=start.get(intervals[i].start,0)+1
            end[intervals[i].end]=end.get(intervals[i].end,0)+1
            timeline.append(intervals[i].start)
            timeline.append(intervals[i].end)
        timeline=list(set(timeline))
        timeline.sort()
        print(start)
        print(end)
        print(timeline)
        for i in range(len(timeline)):
            time=timeline[i]
            count-=end.get(time,0)
            count+=start.get(time,0)
            print(count)
            ans=max(ans,count)
        return ans

        