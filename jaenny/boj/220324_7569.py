from collections import deque

m,n,h = map(int,input().split())

matrix = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visit = [[[-1]*m for _ in range(n)] for _ in range(h)]

ans = -1

queue = deque()

for k in range(h) :
  for i in range(n) :
    for j in range(m) :
      if matrix[k][i][j] == 1 :
        queue.append([k,i,j,0])
        visit[k][i][j] = 0

dk = [-1,1,0,0,0,0]
di = [0,0,0,0,1,-1]
dj = [0,0,1,-1,0,0]


def bfs() :
  while queue :
    k, i, j, cnt = queue.popleft()

    for d in range(6) :
      nk = k + dk[d]
      ni = i + di[d]
      nj = j + dj[d]

      if nk < 0 or nk >= h or ni < 0 or ni >= n or nj < 0 or nj >= m : continue

      if matrix[nk][ni][nj] == 0 and visit[nk][ni][nj] == -1 : # 익지 않은 토마토가 있고, 방문하지 않은 경우라면
        matrix[nk][ni][nj] == 1 # 익은 토마토로 변경
        visit[nk][ni][nj] = cnt + 1 # 방문했음으로 변경
        queue.append([nk,ni,nj,cnt+1]) # 큐에 추가

bfs()

def check() :
  res = 0
  for k in range(h) :
    for i in range(n) :
      for j in range(m) :
        if matrix[k][i][j] == 0 and visit[k][i][j] == -1 : # 익지 않은 토마토가 있는데, 방문하지 못함
          return -1
        else :
          res = max(res, visit[k][i][j])
  return res

print(check())

