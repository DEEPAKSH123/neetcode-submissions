class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output=[]
        intervals.sort(key=lambda x:x[0])
        output.append(intervals[0])
        for start,end in intervals[1:]:
            print(start,end)
            a=output[-1][1]
            if start<=a:
                output[-1][1]=max(a,end)
            else:
                output.append([start,end])
        return output
