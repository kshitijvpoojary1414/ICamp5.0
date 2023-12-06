class ConnectedComponents : 
  def colorConnectedComponents(self, graph) :
    visited = set() 
    color = -1

    for node in graph : 
      if node not in visited :
        self.helper(self, node, graph, color += 1, visited)

    return graph 

  def helper(self, node, graph, color, visited) :
    if node is None :
      return 

    visited.add(node)
    node.color = color 

    for neighbor in neighbors :
      if neighbor not in visited :
        self.helper(neighbor, graph, color, visited)

    return 