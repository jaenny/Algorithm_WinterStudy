from math import inf

def solution(n, results):
  answer = 0

  matrix = [[inf]*n for _ in range(n)] # 승 1, 패 -1, 나 자신 0, 모르는 경우 inf

  for nn in range(n) : # 나 자신은 0
    matrix[nn][nn] = 0

  for result in results :
    a,b = result
    matrix[a-1][b-1] = 1 # 승 
    matrix[b-1][a-1] = -1 # 패
  
  for k in range(n) :
    for i in range(n) :
      for j in range(n) :
        temp = matrix[i][k] + matrix[k][j]
        if temp == inf : continue
        if temp > 0 :
          matrix[i][j] = 1
        elif temp < 0 :
          matrix[i][j] = -1

  for m in matrix :
    if sum(m) == inf : continue
    else : answer += 1

  return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
