from collections import deque
n, m = map(int, input().split())
i,j,d = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]


# 0 - 북쪽, 1 - 동쪽, 2 - 남쪽, 3- 서쪽
# 0, 3, 2, 1 순서로 돈다

cnt = 1
visit[i][j] = 1

di = [-1,0,1,0]
dj = [0,1,0,-1]

while True :
  # 인접지역 탐색
  rotate = 0
  for _ in range(4) :

    ni = i + di[(d+3)%4]
    nj = j + dj[(d+3)%4]

    d = (d+3)%4

    if ni < 0 or ni >= n or nj < 0 or nj >= m : continue
    if matrix[ni][nj] == 0 and visit[ni][nj] == 0 :
      visit[ni][nj] = 1
      cnt+=1
      i, j = ni, nj
      rotate = 1
      break

  if rotate == 0 :
    # print(d)
    if matrix[i - di[d]][j - dj[d]] == 1 :
      print(cnt)
      break
    else :
      i, j = i - di[d], j - dj[d]






