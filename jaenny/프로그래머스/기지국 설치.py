def solution(n, stations, w):
  answer = 0

  start = 1
  d = 2*w + 1
  for station in stations :
    end = station - w - 1
    answer += (end - start + 1) // d
    if (end - start + 1) % d : answer += 1
    start = station + w + 1
  
  if start <= n :
    end = n
    answer += (end - start + 1) // d
    if (end - start + 1) % d : answer += 1

  return answer

print(solution(11, [4,11], 1))
print('----------')
print(solution(16, [9], 2))