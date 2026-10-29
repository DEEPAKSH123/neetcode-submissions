class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for n in stones:
            heapq.heappush(heap,-1*n)
        while len(heap)>1:
            val1=-1*heapq.heappop(heap)
            val2=-1*heapq.heappop(heap)
            print(val1,val2)
            if val1>val2:
                heapq.heappush(heap,-val1+val2)
        return -1*heap[0] if heap else 0

        
        