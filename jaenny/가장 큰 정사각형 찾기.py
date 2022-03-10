def solution(board):
  answer = 0

  height = len(board)
  width = len(board[0]) 

  dp = [[0]*width for _ in range(height)]

  

  for i in range(height) :
    for j in range(width) :
      if board[i][j] == 1 :
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        answer = max(dp[i][j], answer)

  return answer**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))