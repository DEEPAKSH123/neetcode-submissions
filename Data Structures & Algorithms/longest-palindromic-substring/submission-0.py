class Solution:
    def longestPalindrome(self, s: str) -> str:
        st,e=-1,-1
        reslen=0

        for i in range(len(s)):
            left=i
            right=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>reslen:
                    reslen=right-left+1
                    st,e=left,right
                left-=1
                right+=1
            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>reslen:
                    reslen=right-left+1
                    st,e=left,right
                left-=1
                right+=1
        return s[st:e+1]
        