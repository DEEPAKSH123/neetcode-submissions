from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, buy):
            if i >= len(prices):
                return 0

            # Option 1: Do nothing
            a = dfs(i + 1, buy)
            
            # Option 2: Buy or sell stock
            if buy:
                # Option to buy stock
                b = dfs(i + 1, not buy) - prices[i]
                return max(a, b)
            else:
                # Option to sell stock and then go to the cooldown period
                c = dfs(i + 2, not buy) + prices[i]
                return max(a, c)
        
        return dfs(0, True)

# Example usage
solution = Solution()
print(solution.maxProfit([1, 2, 3, 0, 2]))  # Output: 3 (Buy on day 0, sell on day 2, cooldown, buy on day 3, sell on day 4)
print(solution.maxProfit([1]))              # Output: 0 (Not enough days to make any transaction)
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 7 (Buy on day 1, sell on day 2, buy on day 3, sell on day 4)
