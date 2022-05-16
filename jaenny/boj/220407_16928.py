from collections import deque

visit = [False for i in range(101)] # 방문표시

# 사다리 좌표 입력받기
ladder = dict()
n, m = map(int, input().split())
for _ in range(n) :
  x, y = map(int, input().split())
  ladder[x] = y
# 뱀 좌표 입력받기
snake = dict()
for _ in range(m) :
  u, v = map(int, input().split())
  snake[u] = v

queue = deque()
queue.append([1,0])
visit[1] = True

while queue :
  i, cnt = queue.popleft()

  if i == 100 : 
    print(cnt)
    break

  for j in range(1, 7) :
    if i+j > 100 : continue

    if not visit[i+j] : # 주사위 굴린 칸이 아직 방문하지 않은 칸이라면
      if i+j in ladder : # 사다리가 놓여있다면?
        visit[i+j] = True
        visit[ladder[i+j]] = True
        queue.append([ladder[i+j], cnt+1])
      elif i+j in snake : # 뱀이 있다면?
        visit[i+j] = True
        visit[snake[i+j]] = True
        queue.append([snake[i+j], cnt+1])
      else :
        visit[i+j] = True
        queue.append([i+j, cnt+1])
      