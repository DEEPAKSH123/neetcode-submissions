class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache={}

        def dfs(i,total):
            if total==amount:
                return 0
            if i==len(coins) or total>amount:
                return float("inf")
            if (i,total) in cache:
                return cache[(i,total)]
            b=dfs(i+1,total)
            a=1+dfs(i,total+coins[i])
            cache[(i,total)]= min(a,b)
            return cache[(i,total)]
        return dfs(0,0) if dfs(0,0)!=float("inf") else -1
        