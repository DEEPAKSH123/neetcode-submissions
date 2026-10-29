class Solution:
    def numDecodings(self, s: str) -> int:
        v = set(str(i) for i in range(1, 27))
        
        if len(s) == 1:
            return 1 if s[0] in v else 0
        
        n = len(s)
        dp = [0] * n
        
        dp[-1] = 1 if s[-1] in v else 0
        if s[-2] in v:
            dp[-2] = dp[-1]
        if s[-2:] in v:
            dp[-2] += 1

        for i in range(n-3, -1, -1):
            one_digit = s[i]
            two_digit = s[i:i+2]
            a = dp[i+1] if one_digit in v else 0
            b = dp[i+2] if two_digit in v else 0
            dp[i] = a + b
            
        return dp[0]

# Example usage:
# sol = Solution()
# print(sol.numDecodings("226"))  # Output: 3
