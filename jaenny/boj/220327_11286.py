import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []
res=[]

for _ in range(n) :
  x = int(input())
  if x == 0 :
    if len(heap) == 0 :
      print(0)
    else :
      node = heapq.heappop(heap)
      print(node[1])
  else :
    heapq.heappush(heap, [abs(x), x])