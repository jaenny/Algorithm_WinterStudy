from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
answer = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(queue) :
  while queue :
    i, j, h = queue.popleft()

    for d in range(4) :
      ni = i + dy[d]
      nj = j + dx[d]

      if ni < 0 or ni >= n or nj < 0 or nj >= n : continue
      
      if graph[ni][nj] > h and visit[ni][nj] == False :
        visit[ni][nj] = True
        queue.append([ni,nj,h])

for k in range(1,101) :
  temp = 0
  visit = [[False]*n for _ in range(n)]
  for i in range(n) :
    for j in range(n) :
      if graph[i][j] > k and visit[i][j] == False:
        visit[i][j] = True
        temp += 1
        queue = deque()
        queue.append([i,j,k])
        bfs(queue)
  answer = max(answer, temp)

print(answer)