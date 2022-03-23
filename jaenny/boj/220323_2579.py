t = int(input())

stair = [int(input()) for _ in range(t)]

dp = [[0,0] for _ in range(t)]


for i in range(t-1) :
  if i == 0 : dp[0][0] = stair[0]
  elif i == 1 : dp[1][0] = stair[1]

  for j in range(2) :
    score = dp[i][j]
    if j == 0 :
      dp[i+1][1] = max(dp[i+1][1], score+stair[i+1])

    if i+2 < t :
      dp[i+2][0] = max(dp[i+2][0], score+stair[i+2])

if t == 1 :
  print(stair[0])
else :
  print(max(dp[-1]))