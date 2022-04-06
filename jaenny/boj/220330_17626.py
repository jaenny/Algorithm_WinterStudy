import math
n = int(input())

dp = [math.inf]*(n+1)

dp[0] = 0
dp[1] = 1

for i in range(2,n+1) :
  sqrtI = math.sqrt(i)
  if sqrtI == int(sqrtI) : dp[i] = 1
  for j in range(1,int(sqrtI)+1) :
    dp[i] = min(dp[i],dp[i - (j**2)]+1)
print(dp[n])