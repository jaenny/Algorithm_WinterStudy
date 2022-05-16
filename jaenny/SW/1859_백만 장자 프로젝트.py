T = int(input())

for t in range(1,T+1) :
  n = int(input())
  nums = list(map(int,input().split()))

  maxNum = nums[-1]
  total = 0

  for i in range(len(nums)-1,-1,-1) :
    if maxNum <= nums[i] : maxNum = nums[i]
    else :
      total += maxNum - nums[i]
  print("#%d %d" %(t, total))