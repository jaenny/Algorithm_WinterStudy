tc = int(input())

for _ in range(tc) :
  k = int(input())
  n = int(input())

  dp = [[1]*(n+1) for _ in range(k+1)]

  for i in range(k+1) :
    for j in range(1,n+1) :
      if i == 0 :
        dp[i][j] = j
      elif j == 1 :
        dp[i][j] = 1
      else :
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
  print(dp[k][n])