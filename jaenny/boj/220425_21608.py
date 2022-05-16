n = int(input())
info = dict()
for i in range(n**2) :
  new = list(map(int, input().split()))
  info[new[0]] = new[1:]

matrix = [[0]*n for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

for student in info.keys() :
  like = info[student]

  nearLike = []
  for i in range(n) :
    for j in range(n) :
      if matrix[i][j] != 0 : continue

      
      cnt = 0 # 주위의 좋아하는 학생 수
      blankCnt = 0 # 주위의 빈 칸 수
      for d in range(4) :
        ni = i + di[d]
        nj = j + dj[d]

        if ni < 0 or ni >= n or nj < 0 or nj >= n : continue

        if matrix[ni][nj] in like : 
          cnt += 1
        if matrix[ni][nj] == 0 :
          blankCnt += 1
      
      nearLike.append([cnt, blankCnt, i, j])
  
  nearLike.sort(key=lambda x : (-x[0], -x[1], x[2], x[3]))

  matrix[nearLike[0][2]][nearLike[0][3]] = student


# 만족도 구하기
satisfaction = 0
for i in range(n) :
  for j in range(n) :
    temp = 0
    for d in range(4) :
      ni = i + di[d]
      nj = j + dj[d]

      if ni < 0 or ni >= n or nj < 0 or nj >= n : continue

      if matrix[ni][nj] in info[matrix[i][j]] :
        temp += 1
    
    if temp == 1 :satisfaction += 1
    elif temp == 2 : satisfaction += 10
    elif temp == 3 : satisfaction += 100
    elif temp == 4 : satisfaction += 1000

print(satisfaction)