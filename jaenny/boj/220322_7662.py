import sys
import heapq
t = int(input())

def sync(heap) :
  while heap and not visit[heap[0][1]] :
    heapq.heappop(heap)

for _ in range(t) :
  k = int(sys.stdin.readline()) # Q에 적용할 연산의 개수
  maxHeap = []
  minHeap = []
  visit = [False]*1000001

  for i in range(k) :
    op, x = sys.stdin.readline().split()
    x = int(x)
    if op == 'I' :
      heapq.heappush(maxHeap, (-x,i))
      heapq.heappush(minHeap, (x,i))
      visit[i] = True
    elif len(maxHeap) == 0 or len(minHeap) == 0 : continue
    else :
      if x == -1 : # 최솟값 삭제
        visit[minHeap[0][1]] = False
        heapq.heappop(minHeap)
      else : # 최댓값 삭제
        visit[maxHeap[0][1]] = False
        heapq.heappop(maxHeap)
    sync(minHeap)
    sync(maxHeap)
  
  if len(maxHeap) > 0 and len(minHeap) > 0 :
    print(-maxHeap[0][0], minHeap[0][0])
  else :
    print('EMPTY')