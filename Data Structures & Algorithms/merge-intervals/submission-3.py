class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        res.append(intervals[0])

        for i in range(1,len(intervals)):
            start,end = res[-1]
            if intervals[i][0] <=end:
                res[-1][0]=min(start,intervals[i][0])
                res[-1][1]=max(end,intervals[i][1])
            else:
                res.append(intervals[i])
        return res

        