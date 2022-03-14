def solution(n, edges):
  answer = 0

  matrix = [[0]*n for _ in range(n)]

  dic = dict()

  for num in range(n) :
    dic[num] = []

  # 간선 정보 표시
  for edge in edges :
    i,j = edge
    matrix[i][j] = 1
    matrix[j][i] = 1

    dic[i].append(j)
    dic[j].append(i)

  for m in matrix :
    print(m)
  
  for j in range(n) :
    for i in range(n) :
      for k in range(n) :
        if i == j or j == k or i == k : continue
        if dic[i] and matrix[j][k] == 1 and matrix[i][k] == 1:
          if matrix[i][k] == matrix[i][j] + matrix[j][k] :
            answer += 1

  return answer

print(solution(5, [[0,1],[0,2],[1,3],[1,4]]))