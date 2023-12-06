class Dijkstra :
  def dijkstra(self, graph, src, n) :
    distance = [0]*n
    minHeap  = [(0,src)]
    visited = set()

    while len(minHeap) > 0 :
      weight,node = heapq.heappop(minHeap)

      if node in visited :
        continue 

      distance[node] = weight 

      for neighbor in graph[src] :
        nNode, nWeight = neighbor 
        if nNode not in visited :
          heapq.heappush(minHeap, (nWeight + weight,nNode))

    return -1 if len(visited) != n else distance[src]

































class Dijkstra :
  def dijkstra(self, graph, src, n) :
    heap = [(0,src)]
    visited = set() 
    distance = [0]*n

    while len(heap) > 0 :
      weight,node = heapq.heappop(heap) 

      visited.add(node)
      
      distance[node] = weight 

      for neighbor in graph[node] :
        nNode, nWeight = neighbor
        if nNode not in visited :
          heapq.heappush(heap,(weight + nWeight,nNode))


    return -1 if len(visited) != n else distance[src]


    