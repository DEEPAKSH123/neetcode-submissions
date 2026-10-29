class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        ans=[]
        for n in nums:
            count[n]=count.get(n,0)+1
        res=[[] for i in range(len(nums)+1)]
        for number,freq in count.items():
            res[freq].append(number)
        for i in range(len(res)-1,-1,-1):
            for j in res[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans
        return 0

        