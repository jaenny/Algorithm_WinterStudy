def solution(queue1, queue2):

  sum1 = sum(queue1)
  sum2 = sum(queue2)

  s,e = 0,len(queue1)
  cnt = 0
  if (sum1+sum2) % 2 != 0 : return -1

  queue = queue1 + queue2

  while s < len(queue) and e < len(queue) :
    if sum1 == sum2 : return cnt

    if sum1 < sum2 : # e 한 칸 증가
      sum1 += queue[e]
      sum2 -= queue[e]
      e += 1
    elif sum1 > sum2 : # s 한 칸 증가
      sum1 -= queue[s]
      sum2 += queue[s]
      s += 1
    cnt += 1

  return -1


print(solution([3,2,7,2], [4,6,5,1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1,1], [1,5]))
print(solution([1,5], [1,1]))