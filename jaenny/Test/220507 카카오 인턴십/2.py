from collections import deque

def solution(queue1, queue2):
  answer = -1
  visit = dict()

  if (sum(queue1)+sum(queue2)) % 2 != 0 : return -1

  queue = deque()
  queue.append([queue1, queue2, 0])
  
  visit[' '.join(map(str,queue1))] = 1
  visit[' '.join(map(str,queue2))] = 1

  while queue :
    q1, q2, cnt = queue.popleft()
    print(q1, q2, cnt, sum(q1), sum(q2))
    sum1 = sum(q1)
    sum2 = sum(q2)
    if sum1 == sum2 :
      return cnt
    
    # q1 -> q2
    if len(q1) > 0 and sum1 > sum2 :
      # n = q1[0]
      # s1 = ' '.join(map(str,q1[1:]))
      # s2 = ' '.join(map(str,q2+[n]))
      # if s1 not in visit or s2 not in visit: 
      #   visit[s1] = 1
      #   visit[s2] = 1
        # queue.append([q1[1:], q2+[n], cnt+1])
      nsum1 = sum1
      nsum2 = sum2
      for i in range(len(q1)) :
        if nsum2 + q1[i] < nsum1 - q1[i] :
          nsum2 += q1[i]
          nsum1 -= q1[i]
        elif nsum2 + q1[i] == nsum1 - q1[i] :
          return cnt + i + 1
        else :
          if nsum2 + q1[i] == 0 or nsum1 - q1[i] == 0 :
            break
          queue.append([q1[i+1:], q2+q1[:i+1], cnt+i+1])
          break




    # q2 -> q1
    if len(q2) > 0 and sum1 < sum2 :
      # n = q2[0]
      # s1 = ' '.join(map(str,q1+[n]))
      # s2 = ' '.join(map(str,q2[1:]))
      # if s1 not in visit or s2 not in visit : 
      #   visit[s1] = 1
      #   visit[s2] = 1
        # queue.append([q1+[n], q2[1:], cnt+1])
      nsum1 = sum1
      nsum2 = sum2
      for i in range(len(q2)) :
        if nsum1 + q2[i] < nsum2 - q2[i] :
          nsum1 += q2[i]
          nsum2 -= q2[i]
        elif nsum1 + q2[i] == nsum2 - q2[i] : 
          return cnt + i + 1
        else :
          if nsum1 + q2[i] == 0 or nsum2 - q2[i] == 0 :
            break
          queue.append([q1+q2[:i+1], q2[i+1:], cnt+i+1])
          break

  return answer

print(solution([3,2,7,2], [4,6,5,1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1,1], [1,5]))