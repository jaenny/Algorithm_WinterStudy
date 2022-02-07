from collections import deque

def solution(maps):
    answer = 0

    n = len(maps)
    m = len(maps[0])

    queue = deque()

    matrix = []
    visit = [[-1]*m for _ in range(n)] # -1 : 미방문 / 1 이상 : 방문

		# 처음 출발하는 곳을 queue에 넣고, 방문표시
    queue.append([0,0])
    visit[0][0] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue :
      y, x = queue.popleft()

      for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= m or ny <0 or ny >= n : # maps 범위를 넘어가면 pass
          continue
        if maps[ny][nx] == 1 and visit[ny][nx] == -1 : # 갈 수 있는 길이고, 아직 방문 안 했다면
          queue.append([ny,nx])
          visit[ny][nx] = visit[y][x] + 1
        
        if ny == n-1 and nx == m-1 : # 도착지에 최초 방문시 바로 return
          return visit[ny][nx]

    return -1 # while문에서 return 되지 않았다면 도착지까지 갈 수 없는 상태