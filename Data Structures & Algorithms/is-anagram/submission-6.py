class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if len(s)!=len(t):
            return False
        for w in s:
            d1[w]=d1.get(w,0)+1
        for w in t:
            d2[w]=d2.get(w,0)+1
        return d1==d2