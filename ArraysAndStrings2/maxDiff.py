class MaxDiff :
  def BuyAndSellStock1(self, stocks) :
    if stocks is None or len(stocks) == 0 :
      return stocks[0]

    minSoFar = stocks[0]
    result = 0

    for stock in stocks :
      minSoFar = min(minSoFar, stock)
      result = max(result, stock-minSoFar)
    
    return result
  
  def BuyAndSellStock2(self, stocks) :
    bestTillI = []
    bestFromI = []

    result = 0
    minSoFar = prices[0]

    for i in range(len(prices)) :
        minSoFar = min(prices[i], minSoFar)
        result = max(prices[i]- minSoFar, result)
        bestTillI.append(result)

    result = 0
    maxSoFar = prices[-1]
    
    for i in range(len(prices)-1,-1,-1) :
        
        maxSoFar = max(prices[i], maxSoFar)
        result = max(maxSoFar- prices[i], result)
        bestFromI.append(result)

    bestFromI.reverse()
    result = 0
    print(bestTillI, bestFromI)
    for i in range(len(bestTillI)) :
        result = max(result,(bestTillI[i] + bestFromI[i]))


    return result
