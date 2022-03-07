def solution(board):
  answer = 0

  width = min(len(board), len(board[0])) # 정사각형 가로

  def check(i,j) :
    for y in range(i, i+w) :
      for x in range(j, j+w) :
        if board[y][x] == 0 :
          return False
    return True

  for w in range(width, 0, -1 ) :
    for i in range(len(board)-w+1) :
      for j in range(len(board[0])-w+1) :
        if check(i,j) :
          return w*w

  return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))