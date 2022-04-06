from itertools import combinations

def solution(nums):
  r = len(nums)//2
  nums = list(set(nums))

  return len(nums) if r > len(nums) else r

print(solution([3,1,2,3]))
print(solution([3,3,3,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))


