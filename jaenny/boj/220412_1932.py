n = int(input())

matrix =[list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = matrix[0][0]

for i in range(1,n) :
  for j in range(i+1) :
    if j == 0 :
      dp[i][j] = matrix[i][j] + dp[i-1][j]
    elif j == i :
      dp[i][j] = matrix[i][j] + dp[i-1][i-1]
    else :
      dp[i][j] = matrix[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))