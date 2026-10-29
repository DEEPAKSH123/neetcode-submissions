class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=[]
        res.append(intervals[0])
        count=0
        for i in range(1,len(intervals)):
            start,end=res[-1]
            if end>intervals[i][0]:
                res[-1][0]=min(start,intervals[i][0])
                res[-1][1]=min(end,intervals[i][1])
                count+=1
            else:
                res.append(intervals[i])
        return count

        