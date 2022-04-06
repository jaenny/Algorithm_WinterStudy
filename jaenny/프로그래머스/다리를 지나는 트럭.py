from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque() # 다리를 건너는 트럭
    truck_weights = deque(truck_weights)
    passed = deque() # 다리를 지난 트럭
    final = len(truck_weights)

    while True :
      # 1초가 지날 때마다 한 칸씩 전진
      for i in range(len(queue)) :
        queue[i][1] += 1

      # 다리를 다 지난 트럭 빼기
      if len(queue) > 0 :
        first = queue.popleft()
        if first[1] < bridge_length :
          queue.appendleft(first)
        else :
          passed.append(first)

      
      # 대기 트럭에서 다리 건너기
      total = 0
      for q in queue :
        total += q[0]
      if len(truck_weights) > 0 and ( total + truck_weights[0]) <= weight and len(queue) <= bridge_length :
        top = truck_weights.popleft()
        queue.append([top,0])

      answer += 1

      if len(passed) == final :
        return answer



    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))