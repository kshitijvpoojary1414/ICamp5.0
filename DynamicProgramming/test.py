class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [[float('inf') for i in range(amount + 1)] for j in range(len(coins) + 1)]
        self.coinChangeHelper(len(coins), amount, coins, dp)
        
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
    def coinChangeHelper(self, i, j, coins, dp) :
        print(i,j)
        if j == 0 :
            return 0

        if i == 0 :
            return float('inf')

        if dp[i][j] != float('inf') :
            return dp[i][j]

        if coins[i-1] > j :
            value = self.coinChangeHelper(i -1, j, coins, dp)
        else :
            noInclude = self.coinChangeHelper(i -1, j, coins, dp)
            include = 1 + self.coinChangeHelper(i, j - coins[i-1],coins, dp)
            value = min(include, noInclude)

        dp[i][j] = value
        return value
        
        
			
Solution().coinChange([411,412,413,414,415,416,417,418,419,420,421,422],9864)