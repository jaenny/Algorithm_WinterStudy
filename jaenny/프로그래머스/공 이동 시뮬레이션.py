def solution(n, m, x, y, queries):
  answer = 0

  matrix = [[0]*m for _ in range(n)]

  di = [0,0,-1,1]
  dj = [-1,1,0,0]


  ni = 0
  nj = 0
  for d, dx in queries :
    ni = ni + di[d]*dx
    nj = nj + dj[d]*dx

    if ni < 0 : ni = 0
    elif ni >= n : ni = n-1
    elif nj < 0 : nj = 0
    elif nj >= m : nj = m-1

  for i in range(n) :
    for j in range(m) :
      
      if i+ni == x and j+nj == y : answer += 1


  return answer

print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))