class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        h=""
        for i in s:
            if i.isalnum():
                h=h+i
        
        l=0
        r=len(h)-1
        while l<r:
            if h[l]==h[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        
        
        