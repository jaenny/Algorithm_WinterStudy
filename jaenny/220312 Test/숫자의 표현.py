def solution(n):
  answer = 1

  for i in range(1,n+1) :
    cur = i
    for j in range(i+1, n+1) :
      cur += j
      if cur == n :
        answer += 1
      elif cur > n :
        break

  return answer

print(solution(15))