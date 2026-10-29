class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        i=0
        res=1
        
        n=sorted(set(nums))
        print(n)
        if nums==[]:
            return 0
        while i <(len(n)):
            length=1
            print(n[i])
            while (i+1)<len(n) and (n[i]+1)==n[i+1]:
                length+=1
                print("HI")
                res=max(res,length)
                i+=1
            else:
                i+=1
        return res