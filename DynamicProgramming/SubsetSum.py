class SubsetSum :
  def subsetSumRecursive(self, arr, s, n) :
    if n == 0 and s == 0 :
      return True 

    if n == 0 or s == 0 :
      return False 

    if arr[n-1] > s :
      return self.subsetSumRecursive(arr,n-1,s)

    return self.subsetSumRecursive(arr,n-1,s) or arr[n-1] + self.subsetSumRecursive(arr, n-1, s - arr[n-1])

  def subsetSumBottomUp(self, arr, s, n) :
    dp = [[False for i in range(s + 1)] for j in range(len(arr) + 1)]

    for i in range(len(arr)+1) :
      dp[i][0] = True 

    for i in range(s+1) :
      dp[0][i] = False 


    for i in range(len(arr)+1) :
      for s in range(s+1) :
        if arr[i-1] > s :
          dp[i][s] = dp[i-1][s]
        else :
          dp[i][s] = dp[i-1][s] or dp[i-1][s-arr[i-1]]

  def countOfSubsetSum(self, arr, s, n) :
    dp = [[0 for i in range(s + 1)] for j in range(len(n) + 1)]

    for i in range(len(arr)+1) :
      dp[i][0] = 0 
    
    for j in range(s + 1) :
      dp[0][j] = 1 

    for i in range(len(arr)+1) :
      for j in range(s + 1) :
        if arr[i-1] > j :
          dp[i][j] = dp[i-1][j]
        else :
          dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    return dp[-1][-1]

    def equalSumPartition(self, arr) :
      total = sum(arr)

      if total % 2 == 0 :
        return countOfSubsetSum(arr, total//2, len(arr))
      
      return -1

    