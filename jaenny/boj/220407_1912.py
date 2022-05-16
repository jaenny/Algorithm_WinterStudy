n = int(input())
nums = list(map(int, input().split()))

dp = [0]*n

for i in range(n) :
  if i == 0 :
    dp[i] = nums[i]
  else:
    dp[i] = max(nums[i], dp[i-1]+nums[i])

print(max(dp))