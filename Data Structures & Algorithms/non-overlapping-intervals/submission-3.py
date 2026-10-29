class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c=0
        prev=intervals[0][1]
        for start,end in intervals[1:]:
            if start<prev:
                c+=1
                prev=min(prev,end)
            else:
                prev=end
        return c