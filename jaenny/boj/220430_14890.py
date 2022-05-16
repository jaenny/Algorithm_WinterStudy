n, l = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

# 가로 체크
for i in range(n) :
  flag = True
  visit =[0]*n
  for j in range(1, n) :

    if abs(matrix[i][j] - matrix[i][j-1]) == 1 :
      flag = True
      if matrix[i][j] < matrix[i][j-1] :
        now = matrix[i][j]
        for k in range(j, j+l) :
          if k >= n or matrix[i][k] != now or visit[k] == 1 : 
            # 경사로를 놓다가 범위를 벗어남
            # 혹은 l개의 칸이 높이가 동일하지 않은 경우
            flag = False
            break
          else :
            visit[k] = 1
      else :
        now = matrix[i][j-1]
        for k in range(j-l, j) :
          if k < 0 or matrix[i][k] != now or visit[k] == 1: 
            # 경사로를 놓다가 범위를 벗어남
            # 혹은 l개의 칸이 높이가 동일하지 않은 경우
            flag = False
            break
          else :
            visit[k] = 1

    elif abs(matrix[i][j] - matrix[i][j-1]) > 1 :
    # 두 칸의 높이 차가 1 초과
      flag = False
      break

    if flag == False :
      break

  if flag :
    # print(i)
    cnt += 1

# 세로 체크
# print('----')
for j in range(n) :
  flag = True
  visit =[0]*n
  for i in range(1, n) :

    if abs(matrix[i][j] - matrix[i-1][j]) == 1 :
      flag = True
      if matrix[i][j] < matrix[i-1][j] :
        now = matrix[i][j]
        for k in range(i, i+l) :
          if k >= n or matrix[k][j] != now or visit[k] == 1 : 
            # 경사로를 놓다가 범위를 벗어남
            # 혹은 l개의 칸이 높이가 동일하지 않은 경우
            flag = False
            break
          else :
            visit[k] = 1
      else :
        now = matrix[i-1][j]
        for k in range(i-l, i) :
          if k < 0 or matrix[k][j] != now or visit[k] == 1: 
            # 경사로를 놓다가 범위를 벗어남
            # 혹은 l개의 칸이 높이가 동일하지 않은 경우
            flag = False
            break
          else :
            visit[k] = 1

    elif abs(matrix[i][j] - matrix[i-1][j]) > 1 :
    # 두 칸의 높이 차가 1 초과
      flag = False
      break

    if flag == False :
      break

  if flag :
    # print(j)
    cnt += 1

print(cnt)