def quad_tree(x,y,n) :
  color = matrix[y][x]

  for i in range(y, y+n) :
    for j in range(x, x+n) :
      if color != matrix[i][j] :
        res.append('(')
        quad_tree(x, y, n//2)
        quad_tree(x+n//2, y, n//2)
        quad_tree(x, y+n//2, n//2)
        quad_tree(x+n//2, y+n//2, n//2)
        res.append(')')
        return
  
  res.append(str(color))
  return

t = int(input())
matrix = [list(map(int,input())) for _ in range(t)]

res = []
quad_tree(0, 0, t)
print(''.join(res))