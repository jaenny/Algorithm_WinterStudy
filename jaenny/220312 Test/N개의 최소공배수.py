from math import gcd
def solution(arr):
  answer = arr[1]

  for num in arr :
    temp = gcd(answer, num)
    answer = temp * (answer//temp) * (num//temp)

  return answer

print(solution([2,6,8,14]))