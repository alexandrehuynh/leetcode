"""
Leetcode 322. Coin Change: https://leetcode.com/problems/coin-change/description/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Step 1: Initialize the DP array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        # Step 2: Fill the DP table
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # Step 3: Return the result
        return dp[amount] if dp[amount] != float('inf') else -1
    
"""
Time Complexity
	•	O(n * m): Where n is the amount and m is the number of coins.
	•	For each coin, iterate through all amounts from coin to amount.

Space Complexity
	•	O(n): The DP array requires O(amount + 1) space.
"""