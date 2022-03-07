def solution(land):
  answer = 0
  dp = [[0]*4 for _ in range(len(land))]

  for j in range(len(land)) :
    row = land[j]
    for i in range(4) :
      if j == 0 : dp[j][i] = row[i]
      else :
        for k in range(4) :
          if i == k : continue
          dp[j][i] = max(dp[j][i],dp[j-1][k]+row[i])
  
  return max(dp[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))