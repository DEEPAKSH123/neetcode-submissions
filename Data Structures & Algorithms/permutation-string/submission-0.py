class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=[0]*26
        d2=[0]*26
        for i in s1:
            d1[ord(i)-ord('a')]=d1[ord(i)-ord('a')]+1
        k=len(set(s1))
        l=0
        for r in range(len(s2)):
            if (r-l+1)>k:
                d2[ord(s2[l])-ord('a')]-=1
                l+=1
            d2[ord(s2[r])-ord('a')]=d2[ord(s2[r])-ord('a')]+1
            if d1==d2:
                return True
        return False
        