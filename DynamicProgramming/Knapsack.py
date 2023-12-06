class Knapsack :
  def knapsackRecursive(self, value, weight, target, n, memo) :
    if n == 0 or target == 0 :
      return 0 

    if memo[n][target] != -1 :
      return memo[n][target]

    if target < weight[n-1] :
      memo[n][target] =  self.knapsackRecursive(value, weight, target, n - 1 )
    else :
      memo[n][target] = max(self.knapsackRecursive(value,weight, target, n - 1),value[n-1] + self.knapsackRecursive(value,weight, target-weight[n-1], n - 1))

  def knapsackBottomUp(self,value, weight, target, n) :
    #Initialization 
    dp = [[-1 for j in range(len(weight) + 1) ]for i in range(len(value) + 1)]

    for i in range(len(value) + 1) :
      dp[i][0] = 0
  
    for i in range(len(value) + 1) :
      dp[0][i] = 0

    for n in range(len(value) + 1) :
      for w in range(len(weight) + 1) :
          if weight[n-1] > w :
            dp[n][w] = dp[n-1][w]
          else :
            dp[n][w] = max(weight[n][w], value[n-1] + dp[n-1][w-weight[n-1]])

    return weight[-1][-1]