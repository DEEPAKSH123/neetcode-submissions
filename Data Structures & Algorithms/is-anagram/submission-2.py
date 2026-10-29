class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m={}
        for ch in s:
            if ch not in m:
                m[ch]=0
            m[ch]+=1
        a={}
        for ch in t:
            if ch not in a:
               a[ch]=0
            a[ch]+=1
        

        if a==m:
            return True
        return False
            
            

    

        