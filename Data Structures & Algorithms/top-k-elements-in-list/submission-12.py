class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        distr={}
        for n in nums:
            distr[n]=distr.get(n,0)+1
        heap=[]
        for key in distr:
            heapq.heappush(heap,(distr[key],key))
            print(distr[key],key)
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for a,b in heap:
            res.append(b)
        return res
        