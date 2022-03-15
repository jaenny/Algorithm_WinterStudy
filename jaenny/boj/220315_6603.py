from itertools import combinations

def comb(nums) :
  k = nums[0]
  num = nums[1:]

  for c in combinations(num, 6) :
    print(' '.join(map(str,c)))
  print()


while True :
  s = input()
  if s == '0' :
    break

  nums = list(map(int, s.split()))

  comb(nums)
