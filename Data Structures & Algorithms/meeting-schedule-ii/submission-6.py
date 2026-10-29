"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s={}
        e={}
        new=[]
        for i in intervals:
            s[i.start]=s.get(i.start,0)+1
            e[i.end]=e.get(i.end,0)+1
            new.append(i.start)
            new.append(i.end)
        new=sorted(list(set(new)))
        count=0
        ans=0

        for i in range(len(new)):
            if new[i] in e:
                count-=e.get(new[i],0)
            if new[i] in s:
                count+=s.get(new[i],0)
            ans=max(ans,count)
        return ans

            
                