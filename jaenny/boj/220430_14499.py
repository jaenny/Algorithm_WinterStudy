n, m, i, j, k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

orders = list(map(int, input().split()))
dice = [0]*6
res = []
di = [0,0,0,-1,1]
dj = [0,1,-1,0,0]
for order in orders :
  ni, nj = i + di[order], j + dj[order]
  if 0 <= ni < n and 0 <= nj < m :
    new = dice[:]
    if order == 4 : # 남쪽
      new[0] = dice[1]
      new[1] = dice[5]
      new[4] = dice[0]
      new[5] = dice[4]
    elif order == 3 :
      new[0] = dice[4]
      new[1] = dice[0]
      new[4] = dice[5]
      new[5] = dice[1]
    elif order == 1 :
      new[0] = dice[3]
      new[2] = dice[0]
      new[3] = dice[5]
      new[5] = dice[2]
    elif order == 2 :
      new[0] = dice[2]
      new[2] = dice[5]
      new[3] = dice[0]
      new[5] = dice[3]
    
    # 이동한 칸에 쓰여 있는 수가 0 이면
    # 주사위에 복사
    if matrix[ni][nj] == 0 :
      matrix[ni][nj] = new[5]
    else :
      new[5] = matrix[ni][nj]
      matrix[ni][nj] = 0
    
    i, j = ni, nj
    dice = new
    res.append(dice[0])

for r in res :
  print(r)