import math
def solution(n) :
  check = [0]*18
  
  idx = 0
  flag = 0
  for i in range(17, -1, -1) :
    check[i] = n // int(math.pow(3,i))
    if check[i] != 0 and flag == 0: 
      idx = i
      flag = 1
    n = n % int(math.pow(3,i))
    if n == 0 : break

  check = check[:idx+1]
  check.reverse()

  answer = 0
  for i in range(len(check)) :
    answer += check[i] * int(math.pow(3,i))

  return answer
print(solution(45))