n = int(input())
matrix = [[0]*101 for _ in range(101)]

di = [0,-1,0,1]
dj = [1,0,-1,0]

for _ in range(n) :
  j, i, d, g = map(int, input().split())

  matrix[i][j] = 1
  path = [d]

  for gg in range(g+1) :
    if gg == 0 :
      matrix[i+di[d]][j+dj[d]] = 1
      i, j = i+di[d], j+dj[d]
    else :
      new = path[:]
      new.reverse()
      newPath = []
      for p in new :
        p = p+1
        if p > 3 : p = 0
        newPath.append(p)

      for p in newPath :
        i = i + di[p]
        j = j + dj[p]
        matrix[i][j] = 1

      path = path + newPath


res = 0
for i in range(100) :
  for j in range(100) :
    if matrix[i][j] == 1 and matrix[i+1][j] == 1 and matrix[i][j+1] == 1 and matrix[i+1][j+1] == 1 : res +=1
  
print(res)

