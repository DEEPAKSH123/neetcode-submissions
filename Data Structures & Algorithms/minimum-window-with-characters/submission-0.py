class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        have=0
        count={}
        window={}
        for i in t:
            count[i]=count.get(i,0)+1
        need=len(count)
        reslen=float("inf")
        res=[-1,-1]
        l=0
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            if s[r] in count and window[s[r]]==count[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    reslen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in count and count[s[l]]>window[s[l]]:
                    have-=1
                l+=1
        [st,e]=res
        return s[st:e+1]
        