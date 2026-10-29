class Solution:
    def isValid(self, s: str) -> bool:
        d={")":"(",'}':"{","]":'['}
        stack=[]
        for i in range(len(s)):
            if s[i] in d:#closing bracket
                if len(stack)>0 and d[s[i]]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack)==0:
            return True
        else:
            return False