class TopSort :
  def topSort(self, graph) :
    stack = []
    visited = {}

    for node in graph :
      if visited[node] == 0 :
        if not self.helper(node , graph , visited, stack) :
          return []

    return [] 

  def helper(self, node, graph, visited, stack) :
    if node is None :
      return False

    visited[node] = 1 

    for neighbor in graph[node] :
      if visited[neighbor] == 0 :
        if not self.helper(neighbor, graph, visited, stack) :
          return False 
      elif visited[neighbor] == 1 :
        return False 

    visited[node] = 2 
    stack.append(root)

    return True 

  def diameterOfAGraph(self, graph) :
    visited = {}
    stack = []
    for node in graph :
      if node not in visited :
          self.helper(node , graph , visited, stack)

    order = []

    while len(stack) > 0 :
      order.append(stack.pop())

    dp = {node : 0 for node in order}
    diameter = 0 

    while len(order) > 0 :
      node = order.pop()
      diameter = max(dp[node], diameter)

      neighbors = graph[node]

      for neighbor in neighbors :
        dp[neighbor] = max(dp[neighbor],dp[node] + 1 )

    return diameter

class Kahns:
    def topSort(self, edges, n) :
        inDegrees = collections.defaultdict(int)
        graph = collections.defaultdict(list)

        for edge in edges :
            graph[edge[0]].append(edge[1])
            inDegrees[edge[1]] += 1

        queue = []

        for i in range(n) :
            if i not in inDegrees :
                queue.append(i)

        queue.append('#')
        count = 0
        processed = 0
        while len(queue) > 0 :
            node = queue.pop(0)

            if node == "#" :
                if len(node) > 0:
                    queue.append("#")
                    count += 1 
            processed += 1
            neighbors = graph.get(node, [])

            for neighbor in neighbors :
                inDegrees[neighbor] -= 1 
                if inDegrees[neighbor] == 0 :
                    queue.append(neighbor)

        
        return count if processed == n else -1

