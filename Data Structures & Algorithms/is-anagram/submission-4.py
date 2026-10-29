class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if len(s)!=len(t):
            return False
        for i in s:
            d1[i]=d1.get(i,0)+1
        for i in t:
            d2[i]=d2.get(i,0)+1
        return d1==d2
        