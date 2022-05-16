from collections import deque
matrix = []
n = 0
m = 0
def solution(board) :
  answer = 0
  global matrix, n, m
  matrix = board
  n = len(matrix)
  m = len(matrix[0])


  # 세로
  
  for j in range(m) :
    visit = [[0]*m for _ in range(n)]
    r = bfs(0,j,'down',visit)
    answer = max(answer, r)
    print(j, r)
    print('------------')
  
  for i in range(n) :
    visit = [[0]*m for _ in range(n)]
    r = bfs(i,0,'right',visit)
    answer = max(answer, r)
    print(i, r)
    print('------------')
  
  return answer

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def bfs(i,j,direction,visit) :
  cnt = 0
  queue = deque()
  if direction == 'down' :
    for i in range(len(visit)) :
      if visit[i][j] == 0 :
        visit[i][j] = 1
        queue.append([i,j])
        target = matrix[i][j]
        cnt += 1
        while queue :
          print(queue)
          y,x = queue.popleft()

          for d in range(4) :
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<= ny < n and 0<= nx < m and visit[ny][nx] == 0 and matrix[ny][nx] == target :
              visit[ny][nx] = 1
              cnt += 1
              queue.append([ny,nx])
  else :
    for j in range(len(visit[0])) :
      if visit[i][j] == 0 :
        visit[i][j] = 1
        queue.append([i,j])
        target = matrix[i][j]
        cnt += 1
        while queue :
          y,x = queue.popleft()

          for d in range(4) :
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<= ny < n and 0<= nx < m and visit[ny][nx] == 0 and matrix[ny][nx] == target :
              visit[ny][nx] = 1
              cnt += 1
              queue.append([ny,nx])
  
  return cnt



# print(solution(["DDCCC","DBBBC","DBABC","DBBBC","DDCCC"]))
print(solution(["ABBBBC","AABAAC","BCDDAC","DCCDDE","DCCEDE","DDEEEB"]))