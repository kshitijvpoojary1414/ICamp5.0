class Bipartite :
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes = {"odd" : [], "even" : []}
        visited = {}


        for i in range(len(graph)) :
            if i not in visited :
                if not self.helper(i, graph, nodes, visited) :
                    return False

        return True
    def helper(self, root, graph, nodes, visited) :
        if root is None :
            return False 

        queue = [(root,0)]
        visited[root] = 0

        while len(queue) > 0 :
            node, currentLevel = queue.pop(0)
            neighbors = graph[node]
            for neighbor in neighbors :
                if neighbor not in visited :
                    queue.append((neighbor, currentLevel + 1))
                    visited[neighbor] = currentLevel + 1
                elif  visited[neighbor] == currentLevel :
                    print("Failig",neighbor, node)
                    return False 

        return True 

  