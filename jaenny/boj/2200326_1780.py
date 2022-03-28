n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]
res = []

def quad_tree(x,y,n) :
  num = matrix[y][x]

  for i in range(y, y+n) :
    for j in range(x, x+n) :
      if matrix[i][j] != num :
        quad_tree(x, y, n//3)
        quad_tree(x+n//3, y, n//3)
        quad_tree(x+n//3*2, y, n//3)
        quad_tree(x, y+n//3, n//3)
        quad_tree(x, y+n//3*2, n//3)
        quad_tree(x+n//3, y+n//3, n//3)
        quad_tree(x+n//3*2, y+n//3, n//3)
        quad_tree(x+n//3, y+n//3*2, n//3)
        quad_tree(x+n//3*2, y+n//3*2, n//3)
        return
  
  res.append(num)
  return


quad_tree(0,0,n)
print(res.count(-1))
print(res.count(0))
print(res.count(1))