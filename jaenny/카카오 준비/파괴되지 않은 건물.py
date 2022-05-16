def solution(board, skill):
  answer = 0

  _sum = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

  for t, r1, c1, r2, c2, degree in skill :
    if t == 1 :
      degree = (-1) * degree 

    _sum[r1][c1] += degree
    _sum[r2+1][c2+1] += degree
    _sum[r1][c2+1] += (-1)*degree
    _sum[r2+1][c1] += (-1)*degree

  # 누적합
  # 오른쪽으로 -> 아래로
  for t in range(2) :
    if t == 0 :
      for i in range(len(board)) :
        for j in range(len(board[0])) :
          _sum[i][j+1] += _sum[i][j]
    else :
      for i in range(len(board)) :
        for j in range(len(board[0])) :
          _sum[i+1][j] += _sum[i][j]
  
  for i in range(len(board)) :
    for j in range(len(board[0])) :
      if board[i][j] + _sum[i][j] >= 1 : answer += 1

  return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))