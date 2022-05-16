import heapq
from math import inf

V, E = map(int, input().split())

start = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E) :
  u, v, w = map(int, input().split())
  graph[u].append((v,w)) # 목적지, 가중치

def dijkstra(graph, start) :
  distances = {x : inf for x in range(1,V+1)}
  distances[start] = 0

  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue :
    currentDistance, currentDestination = heapq.heappop(queue)

    if distances[currentDestination] < currentDistance :
      continue

    for newDestination, newDistance in graph[currentDestination] :
      distance = currentDistance + newDistance
      if distance < distances[newDestination] :
        distances[newDestination] = distance
        heapq.heappush(queue, [distance, newDestination])
  
  return distances

distances = dijkstra(graph, start)

for node in distances :
  if distances[node] == inf :
    print('INF')
  else :
    print(distances[node])