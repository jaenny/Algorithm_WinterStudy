from collections import defaultdict
n, k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
# 0 : 흰색, 1 : 빨간색, 2 : 파란색

chess = [[[] for _ in range(n)] for _ in range(n)]

dic = defaultdict(list) # dic[1] = [2,3] : 1번 말은 y = 2, x = 3 에 위치

directions = [[0,1],[0,-1],[-1,0],[1,0]]

for kk in range(k) :
  i, j, d = map(int, input().split())
  i, j, d = i-1, j-1, d-1
  chess[i][j].append([kk+1, d])
  dic[kk+1] = [i,j]

cnt = 0
flag = False

def white(i,j,ni,nj) :
  chess[ni][nj].extend(chess[i][j])
  chess[i][j] = []

def red(i,j,ni,nj) :
  chess[i][j] = reversed(chess[i][j])
  chess[ni][nj].extend(chess[i][j])
  chess[i][j] = []

def moveTogether(ni,nj) :
  for num, dd in chess[ni][nj] :
    dic[num] = [ni,nj]

while 1 :
  if cnt > 1000 : 
    print(-1)
    break
  cnt += 1

  for kk in dic.keys() : # 1번 말의 위치부터 순회
    i,j = dic[kk]

    if chess[i][j][0][0] != kk : continue # 가장 아래에 kk번째 말이 있지 않다면 -> pass
    else : # 가장 아래에 kk번째 말이 있다면 -> 이동
      d = chess[i][j][0][1] # 이동할 방향

      # 이동할 위치
      ni = i + directions[d][0] 
      nj = j + directions[d][1]

      if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 0 :
        # 이동하려는 칸이 흰색
        white(i,j,ni,nj)
        moveTogether(ni, nj)

      elif 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 1 :
        # 이동하려는 칸이 빨간색
        red(i,j,ni,nj)
        moveTogether(ni, nj)
      
      else :
        # 이동하려는 칸이 파란색
        # 방향을 반대로 한다.
        if d == 0 : chess[i][j][0][1] = 1
        elif d == 1 : chess[i][j][0][1] = 0
        elif d == 2 : chess[i][j][0][1] = 3
        elif d == 3 : chess[i][j][0][1] = 2

        d = chess[i][j][0][1]

        # 한 칸을 이동할 수 있으면 한다.
        ni = i + directions[d][0]
        nj = j + directions[d][1]

        if ni < 0 or ni >= n or nj < 0 or nj >= n or matrix[ni][nj] == 2 : # 이동 불가능 or 파란칸
          ni, nj = i, j
        elif matrix[ni][nj] == 0 : # 하얀칸
          white(i,j,ni,nj)
          moveTogether(ni, nj)
        elif matrix[ni][nj] == 1 : # 빨간칸
          red(i,j,ni,nj)
          moveTogether(ni, nj)

      if len(chess[ni][nj]) >= 4 :
        print(cnt)
        flag = True 
        break

  if flag : break
