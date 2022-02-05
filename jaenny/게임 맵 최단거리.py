from collections import deque

def solution(maps):
    answer = 0

    n = len(maps)
    m = len(maps[0])

    queue = deque()

    matrix = []
    visit = [[-1]*m for _ in range(n)]
    queue.append([0,0])
    visit[0][0] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue :
      y, x = queue.popleft()

      for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= m or ny <0 or ny >= n :
          continue
        if maps[ny][nx] == 1 and visit[ny][nx] == -1 :
          queue.append([ny,nx])
          visit[ny][nx] = visit[y][x] + 1
        
        if ny == n-1 and nx == m-1 :
          return visit[ny][nx]

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))