from math import inf
def solution(N, road, K):
  matrix = [[inf]*N for _ in range(N)]
  
  # 마을 간의 거리 정보 입력받기
  for r in road :
    i, j, d = r
    i -= 1
    j -= 1
    matrix[i][j] = min(matrix[i][j], d)
    matrix[j][i] = min(matrix[j][i], d)

  # 플로이드 와샬 
  for k in range(N) :
    matrix[k][k] = 0 
    for i in range(N) :
      for j in range(N) :
        matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

  # 1번 마을에서 다른 마을까지의 거리가 K이하이면 +1
  answer = 0
  for x in matrix[0] :
    if x <= K : answer +=1
  
  return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))