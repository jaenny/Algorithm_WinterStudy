di = [-1,-1,-1,-1,0,1,2,2,2,2,1,0]
dj = [-1,0,1,2,2,2,2,1,0,-1,-1,-1]

bi = []

def hall(matrix,rooms,baths) : # 최소 한 방향은 복도랑 연결
  for room in rooms :
    roomFlag = False
    i,j = room
    for d in range(12) :
      ni = i + di[d]
      nj = j + dj[d]

      if 0 < ni or ni >= len(matrix) or 0 < nj or nj >= len(matrix[0]) : continue
      if matrix[ni][nj] == 0 : # 복도라면
        roomFlag = True
        break
    if roomFlag == False :
      return False
  
  for bath in baths :
    bathFlag = False
    i,j = bath

  return True

def solution(n, m, room, bath) :
  answer = 0

  rooms = [[0,0],[0,3]]
  baths = [[2,4]]
  hall(matrix,roods,baths)

  return 1


print(solution(4, 5, 3, 1))
print(solution(2, 3, 1, 1))
print(solution(3, 4, 2, 1))
print(solution(2, 3, 1, 1))