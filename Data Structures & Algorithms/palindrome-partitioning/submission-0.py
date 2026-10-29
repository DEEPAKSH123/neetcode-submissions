class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curset=[]
        res=[]
        def palindrome(a):
            return a==a[::-1]
        def dfs(i):
            if i==len(s):
                res.append(curset.copy())
                return
            for j in range(i,len(s)):
                if palindrome(s[i:j+1]):
                    curset.append(s[i:j+1])
                    dfs(j+1)
                    curset.pop()
        dfs(0)
        return res

    
        