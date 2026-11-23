class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if(len(s)!=len(t)):
            return False
        for word in s:
            d1[word]=d1.get(word,0)+1
        for word in t:
            d2[word]=d2.get(word,0)+1
        return d1==d2
        