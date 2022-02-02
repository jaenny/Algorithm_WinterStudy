import copy

def rotate(arr, matrix, mins) :
  sy, sx, ey, ex = arr

  sy -=1
  sx -=1
  ey -=1
  ex -=1

  nums = 10000000000000

  rightTop = matrix[sy][ex]
  leftBottom = matrix[ey][sx]
  rightBottom = matrix[ey][ex]

  nums = min([nums, rightTop, rightBottom, leftBottom])


  # 위쪽
  for i in range(ex-sx,0,-1) :
    matrix[sy][sx+i] = matrix[sy][sx+i-1]
    nums = min(nums, matrix[sy][sx+i-1])

  # 오른쪽
  for i in range(ey-sy,0,-1) :
    if i == 1 :
      matrix[sy+i][ex] = rightTop
    else :
      matrix[sy+i][ex] = matrix[sy+i-1][ex]
      nums = min(nums, matrix[sy+i-1][ex])

  # 아래쪽
  for i in range(0, ex-sx) :
    if i == ex-sx-1 :
      matrix[ey][sx+i] = rightBottom
    else :
      matrix[ey][sx+i] = matrix[ey][sx+i+1]
      nums = min(nums, matrix[ey][sx+i+1])
  
  # 왼쪽
  for i in range(0, ey-sy) :
    if i == ey-sy-1 :
      matrix[sy+i][sx] = leftBottom
    else :
      matrix[sy+i][sx] = matrix[sy+i+1][sx]
      nums = min(nums, matrix[sy+i+1][sx])

  mins.append(nums)
  return matrix


def solution(rows, columns, queries):
    answer = []
    
    matrix = [[0 for col in range(columns)] for row in range(rows)]

    val = 1
    for i in range(0, rows):
        for j in range(0, columns):
            matrix[i][j] = val
            val+=1
    
    for q in queries :
      matrix = rotate(q, matrix, answer)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))