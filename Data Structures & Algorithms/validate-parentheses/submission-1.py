class Solution:
    def isValid(self, s: str) -> bool:
        d={']':'[','}':'{',')':'('}
        stack=[]
        i=0
        while i<len(s):
            if s[i] in d:
                if stack and stack[-1]==d[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            i+=1
        return True if not stack else False