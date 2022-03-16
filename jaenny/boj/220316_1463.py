from math import inf
n = int(input())
dp = [0]*(n+1)

for i in range(2,n+1) :
  r3, r2, r1 = inf, inf, inf

  if i%3 == 0 :
    r3 = 1 + dp[i//3]
  if i % 2 == 0 :
    r2 = 1 + dp[i//2]

  r1 = 1 + dp[i-1]

  dp[i] = min(r3, r2, r1)

print(dp[n])
