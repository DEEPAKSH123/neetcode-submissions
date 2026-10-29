class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ma={}
        for i in range(n):
            ma[i]=[]
        for a,b in edges:
            ma[a].append(b)
            ma[b].append(a)
        visit=set()
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for neig in ma[i]:
                if neig==prev:
                    continue
                if dfs(neig,i)==False:
                    return False
            return True
        a=dfs(0,-1)
        if len(visit)!=n:
            return False
        return a
        