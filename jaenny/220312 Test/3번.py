def solution(width, height, diagonals):
  answer = 0        

  matirx = [[1]*(width+1) for _ in range(height+1)]

  point = []
  for dia in diagonals :
    y,x = dia[1], dia[0]
    point.append([[y-1,x],[y,x-1]])

  def shortest(start, end) :
    dp = [[1]*(end[1]-start[1]+1) for _ in range(end[0]-start[0]+1)]

    for i in range(len(dp)) :
      for j in range(len(dp[0])) :
        if i-1 < 0 or j-1 < 0 : continue
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
    
    return dp[-1][-1]

  for p in point :
    # 위로 먼저 접근
    _up = 0
    _up += shortest([0,0], p[0])
    _up *= shortest(p[1], [height, width])

    # 아래로 먼저 접근
    _down = 0
    _down += shortest([0,0], p[1])
    _down *= shortest(p[0], [height, width])
  
    answer = answer + _up + _down

  return answer % 10000019

print(solution(2, 2, [[1,1],[2,2]]))
print(solution(51, 37, [[17,19]]))