class DetectingCycle :
  def detectCycle(self, graph) :
    visited = {}

    for node in graph :
      if not not in visited and visited[node] == 0 :
        if self.helper(node, graph, visited) :
          return True 

    return False 

  def helper(self, node, graph, visited) :
    if node is None :
      return False 

    visited[node] = 1 

    for neighbor in graph[node] :
      if neighbor not in visited :
        if self.helper(neighbor, graph, visited) :
          return True 
      elif visited[neighbor] == 1 :
        return True 

    visited[node] = 2

    return False 