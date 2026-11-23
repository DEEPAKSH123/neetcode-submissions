class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        first=2
        sec=1
        for i in range(n-3,-1,-1):
            temp=first+sec
            sec=first
            first=temp
        
        return first
        