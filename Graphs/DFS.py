class DFS :
  def dfs(self, root, target ,graph, visited) :
    if self.root is None :
      return False 

    if root == target :
      return True 

    visited.add(root)

    neighbors = graph[root]

    for neighbor in neighbors :
      if neighbor not in visited :
        if self.dfs(neighbor, target ,graph, visited) :
          return True 

    return False

  def cloneGraph(self, node: 'Node') -> 'Node':
      if node is None :
          return None 
      newNode = Node(node.val)
      visited = set()
      nodeMap = {node : newNode}
      self.cloneGraphHelper(node, nodeMap, visited)
      return newNode

  def cloneGraphHelper(self, root, nodeMap, visited) :
      if root is None :
          return 
      
      visited.add(root)

      neighbors = root.neighbors 

      for neighbor in neighbors :
          newNode = None 
          if neighbor in nodeMap :
              newNode = nodeMap[neighbor]
          else :
              newNode = Node(neighbor.val)
              nodeMap[neighbor] = newNode 
          nodeMap[root].neighbors.append(newNode)
          if neighbor not in visited :
              self.dfs(neighbor, nodeMap, visited)