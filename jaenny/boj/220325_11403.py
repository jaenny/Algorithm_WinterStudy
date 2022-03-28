n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
for k in range(n) : # 경유지
  for i in range(n) : # 출발지
    for j in range(n) : # 도착
      if (matrix[i][k] == 1 and matrix[k][j] == 1) :
        matrix[i][j] = 1

for m in matrix :
  print(' '.join(map(str,m)))