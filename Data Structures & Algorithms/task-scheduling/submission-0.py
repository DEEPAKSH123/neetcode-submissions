class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap=[]
        freq={}
        for a in tasks:
            freq[a] = freq.get(a,0) + 1
        for key,value in freq.items():
            heapq.heappush(heap,-value)
        q=deque()
        curTime=0
        while heap or q:
            curTime+=1
            if heap:
                ele = heapq.heappop(heap)
                newCount=ele+1
                if newCount:
                    newTime=curTime+n
                    q.append([newCount,newTime])
            if q:
                if curTime == q[0][1]:
                    c=q.popleft()[0]
                    heapq.heappush(heap,c)
        return curTime
        