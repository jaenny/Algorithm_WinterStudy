def solution(rc, operations):

  for op in operations :
    if op == 'ShiftRow' :
      rc = [rc[-1]]+rc[:-1]
    else :
      top, left, bottom, right = 0, 0, len(rc)-1, len(rc[0])-1    
      temp = rc[top][left]
  
      for k in range(top, bottom):    # 1번
          rc[k][left] = rc[k + 1][left]
  
      for k in range(left, right):    # 2번
          rc[bottom][k] = rc[bottom][k + 1]
  
      for k in range(bottom, top, -1):    # 3번
          rc[k][right] = rc[k - 1][right]
  
      for k in range(right, left, -1):    # 4번
          rc[top][k] = rc[top][k - 1]
  
      rc[top][left + 1] = temp    # temp 넣기

  return rc
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 	["Rotate", "ShiftRow"]))