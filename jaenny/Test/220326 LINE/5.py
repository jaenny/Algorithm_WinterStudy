def solution(abilities, k):
  answer = 0

  abilities.sort(reverse=True)
  dp = [[0]*(k+1) for _ in range((len(abilities)+1)//2)]
  i = 0
  while i < (len(abilities)+1)//2 :
    # print(i)
    if i == 0 :
      dp[i][0] = abilities[i*2+1]
      dp[i][1] = abilities[i*2]
    else :
      for j in range(k+1) :
        if j == 0 :
          if i*2+1 < len(abilities) :
            dp[i][j] = dp[i-1][j] + abilities[i*2+1]
          else :
            dp[i][j] = dp[i-1][j]
        elif j > 0 :
          if i*2+1 < len(abilities) :
            dp[i][j] = max(dp[i-1][j-1]+abilities[i*2], dp[i-1][j]+abilities[i*2+1])
          else :
            dp[i][j] = max(dp[i-1][j-1]+abilities[i*2], dp[i-1][j])
    i += 1
  return max(dp[-1])

print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))
print(solution([7, 6, 8, 9, 10], 1))