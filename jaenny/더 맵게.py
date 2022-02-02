import heapq

def solution(scoville, K):
  answer = 0

  heapq.heapify(scoville)
  while True :

    a = heapq.heappop(scoville)
    b = heapq.heappop(scoville)
    new = a + b*2
    heapq.heappush(scoville, new)
    # print(scoville)

    answer += 1
    c = heapq.heappop(scoville)
    if c >= K :
      return answer
    else :
      heapq.heappush(scoville, c)
      if len(scoville) == 1 :
        return -1

print(solution([1, 2, 3, 9, 10, 12], 100))