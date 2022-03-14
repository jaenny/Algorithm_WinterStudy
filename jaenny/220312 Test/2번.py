def solution(n, clockwise):
  answer = []

  matrix = [[0]*n for _ in range(n)]

  leftUp = [0,0]
  rightUp = [0,n-1]
  leftDown = [n-1,0]
  rightDown = [n-1,n-1]

  counts = [n-1]
  c = n-1
  while True :
    if c == 2 :
      counts.append(1)
      break
    if c < 2 : break
    counts.append(c-2)
    c -= 2

  num = 1

  def insert(startY, startX, count, startNum, d) :
    if d == 'R' :
      for j in range(count) :
        matrix[startY][startX+j] = startNum + j
      if clockwise : return [startY+1, startX+j]
      return [startY-1, startX+j]
    elif d == 'D' :
      for i in range(count) :
        matrix[startY+i][startX] = startNum + i
      if clockwise : return [startY+i, startX-1]
      return [startY+i, startX+1]
    elif d == 'L' :
      for j in range(count) :
        matrix[startY][startX-j] = startNum + j
      if clockwise : return [startY-1, startX-j]
      return [startY+1, startX-j]
    else :
      for i in range(count) :
        matrix[startY-i][startX] = startNum + i
      if clockwise : return [startY-i, startX+1]
      return [startY-i, startX-1]


  if clockwise :
    direction = 'RDLU'
    for i in range(len(counts)) :
    # 왼쪽 위에
      leftUp = insert(leftUp[0],leftUp[1], counts[i], num, direction[i%4])

    # 오른쪽 위에
      rightUp = insert(rightUp[0],rightUp[1], counts[i], num, direction[(i+1)%4])

    # 오른쪽 아래
      rightDown = insert(rightDown[0],rightDown[1], counts[i], num, direction[(i+2)%4])

    # 왼쪽 아래
      leftDown = insert(leftDown[0],leftDown[1], counts[i], num, direction[(i+3)%4])

      num += counts[i]

  else :
    direction = 'DRUL'
    for i in range(len(counts)) :
    # 왼쪽 위에
      leftUp = insert(leftUp[0],leftUp[1], counts[i], num, direction[i%4])

    # 오른쪽 위에
      rightUp = insert(rightUp[0],rightUp[1], counts[i], num, direction[(i+3)%4])

    # 오른쪽 아래
      rightDown = insert(rightDown[0],rightDown[1], counts[i], num, direction[(i+2)%4])

    # 왼쪽 아래
      leftDown = insert(leftDown[0],leftDown[1], counts[i], num, direction[(i+1)%4])

      num += counts[i]



  return matrix

print(solution(9, False))