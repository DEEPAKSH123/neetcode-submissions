class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for n in stones:
            heapq.heappush(heap,-n)
        while len(heap)>=2:
            first=-heapq.heappop(heap)
            sec=-heapq.heappop(heap)
            new=abs(first-sec)
            if new!=0:
                heapq.heappush(heap,-new)
        return -heap[0] if len(heap)==1 else 0
        