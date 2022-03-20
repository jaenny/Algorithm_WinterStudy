import math

n, m, b = list(map(int,input().split()))
matrix = [list(map(int,input().split())) for _ in range(n)]

times = [math.inf, 0]

for h in range(0,257) :
  temp = 0
  delete = 0
  put = 0
  for i in range(n) :
    for j in range(m) :
      if matrix[i][j] == h : 
        continue
      elif matrix[i][j] > h : # 제거
        delete += matrix[i][j] - h
      else : # 놓기
        put += h - matrix[i][j]

  # 인벤토리의 상자 수 보다 놓아야 할 상자수가 많은 경우 => continue
  if delete+b < put : 
    continue
  
  # 제거는 2초 놓기는 1초
  t = delete*2 + put

  if t < times[0] :
    times = [t,h]
  elif t == times[0] : # 최소 시간이 같다면
    if h > times[1] : # 더 높은 층으로 update
        times[1] = h

print(times[0],times[1])