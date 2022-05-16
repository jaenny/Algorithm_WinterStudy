import heapq
def solution(operations):
  answer = []

  index = [0]*1000000
  maxHeap = []
  minHeap = []
  i = 0

  def sync(heap) :
    while heap and not index[heap[0][1]] :
      heapq.heappop(heap)

  for op in operations :
    o,n = op.split()
    n = int(n)
    if o == 'I' :
      heapq.heappush(maxHeap, [-n,i])
      heapq.heappush(minHeap,[n,i])
      index[i] = 1
      i += 1
    elif n == 1 :
      if len(maxHeap) == 0 : continue
      nn, ii = heapq.heappop(maxHeap)
      index[ii] = 0 # 삭제된 숫자
      sync(minHeap)
    else :
      if len(minHeap) == 0 : continue
      nn, ii = heapq.heappop(minHeap)
      index[ii] = 0 # 삭제된 숫자
      sync(maxHeap)
  sync(maxHeap)
  sync(minHeap)
  if len(maxHeap) > 0 and len(minHeap) > 0 :
    return [-maxHeap[0][0], minHeap[0][0]]
  else :
    return [0,0]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I 7","I 5","I -5","D -1"]))