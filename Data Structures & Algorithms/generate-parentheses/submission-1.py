class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output=[]
        def dfs(res,open,close):
            if open>n or close>n or len(res)>2*n:
                return
            if len(res)==2*n:
                if open==close==n:
                    output.append(res)
                    return
            dfs(res+"(",open+1,close)
            if close<open:
                dfs(res+")",open,close+1)
        dfs("",0,0)
        return output

        