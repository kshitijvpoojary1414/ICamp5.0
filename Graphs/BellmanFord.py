class BellmanFord :
  def bellmanFord(self, src, dest, edges, n) :
    distance = [float('inf')]*n
    distance[src] = 0

    for i in range(n + 1) :
      previous = distance[::]
      for edge in edges :
        src, dest, weight = edge 
        if previous[src] != float('inf') and previous[src] + weight < distance[dest] :
          distance[dest] = previous[src] + weight 

    for edge in edges :
      src, dst, weight = edge
      if previous[src] != float('inf') and previous[src] + weight < current[dst]:
        print("Negative cycle")

    return distance[dest]


class BellmanFord :
  def bellmanFord(self, src, dest, edges, n) :
    dp = [float('inf')]*n
    dp[src] = 0 

    for i in range(n+1) :
      previous = dp[::]
      for edge in edges :
        cSrc, cDest,cWeight = edge
        if previous[cSrc] != float('inf') and previous[cSrc] + cWeight < dp[cDest] :
          dp[cDest] = previous[cSrc] + cWeight
    for edge in edges :
      src, dst, weight = edge
      if previous[src] != float('inf') and previous[src] + weight < current[dst]:
        print("Negative cycle")
    return dp[dest]