class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap=[]
        for x,y in points:
            d=(x*x) +(y*y)
            heapq.heappush(maxHeap,(-d,(x,y)))
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        res=[]
        while len(maxHeap)>0:
            a,b=heapq.heappop(maxHeap)
            res.append(b)
        return res
            
