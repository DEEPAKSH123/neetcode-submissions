class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=[]
        count=0
        intervals.sort()
        if not intervals:
            return 0
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[-1][1]>intervals[i][0]:
                res[-1][0]=min(res[-1][0],intervals[i][0])
                res[-1][1]=min(res[-1][1],intervals[i][1])
                count+=1
            else:
                res.append(intervals[i])
        return count