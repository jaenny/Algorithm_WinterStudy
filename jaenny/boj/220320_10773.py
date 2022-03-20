n = int(input())

nums = []

for _ in range(n) :
  new = int(input())
  
  if new == 0 :
    nums.pop()
  else :
    nums.append(new)

if len(nums) == 0 :
  print(0)
else :
  print(sum(nums))