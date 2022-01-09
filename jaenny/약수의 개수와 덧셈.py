def solution(left, right):
  answer = 0

  for num in range(left, right+1) :
    temp = divisor(num)
    print(num, temp)
    if temp % 2 == 0 :
      answer += num
    else :
      answer -= num
  return answer

def divisor(n) :
  divisorList = []
  i = 1
  while i*i <= n :
    if n % i == 0 :
      divisorList.append(i)
      if i != n//i : divisorList.append(n//i)
    i+=1
  
  return len(divisorList)

print(solution(1000,1000))