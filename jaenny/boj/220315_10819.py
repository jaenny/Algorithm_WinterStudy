from itertools import permutations

n = int(input())
nums = list(map(int,input().split()))

res = 0
for per in permutations(nums):
  temp = 0
  for i in range(n-1) :
    temp += abs(per[i]-per[i+1])
  res = max(res,temp)

print(res)