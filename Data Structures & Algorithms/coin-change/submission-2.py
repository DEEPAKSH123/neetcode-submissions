from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP table with a large number representing infinity
        dp = [[amount + 1] * (amount + 1) for _ in range(len(coins))]
        
        # Base case: amount of 0 requires 0 coins
        for i in range(len(coins)):
            dp[i][0] = 0
        
        # Base case for the first row
        for j in range(1, amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = j // coins[0]

        # Fill the DP table
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                a = float('inf')
                if j - coins[i] >= 0:
                    a = 1 + dp[i][j - coins[i]]
                b = dp[i - 1][j]
                dp[i][j] = min(a, b)
        
        # Check the result for the full amount
        return dp[-1][amount] if dp[-1][amount] <= amount else -1
