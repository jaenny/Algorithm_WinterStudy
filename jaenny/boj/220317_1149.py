n = int(input())

costs = [list(map(int,input().split())) for _ in range(n)]

dp = [[costs[0][0],costs[0][1],costs[0][2]]]+[[0,0,0] for _ in range(n-1)]

for i in range(1,len(costs)) :
  cost = costs[i]
  for j in range(3) :
    if j == 0 :
      dp[i][j] += cost[j] + min(dp[i-1][1], dp[i-1][2])
    elif j == 1 :
      dp[i][j] += cost[j] + min(dp[i-1][0], dp[i-1][2])
    else :
      dp[i][j] += cost[j] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))