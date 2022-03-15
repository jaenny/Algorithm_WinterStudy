n = int(input())
nums = list(map(int,input().split()))

def ans(nums):
  for i in range(len(nums)-1, 0, -1) :
    prev = nums[i-1]
    for j in range(len(nums)-1, i-1, -1) :
      if nums[j] > nums[i-1] :
        nums[i-1], nums[j] = nums[j], nums[i-1]
        temp = nums[i:]
        temp.reverse()
        return  ' '.join(map(str,nums[:i]+temp))

  return -1 # 모든 for문을 돌았는데 return문에 걸리지 않았다면 -1

print(ans(nums))