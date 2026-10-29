class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for n in strs:
            res+=(str(len(n))+"*"+n)
        return res


    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            k=i
            while s[k]!="*":
                k+=1
            length=int(s[i:k])
            word=s[k+1:k+1+length]
            ans.append(word)
            i=k+1+length
        return ans
