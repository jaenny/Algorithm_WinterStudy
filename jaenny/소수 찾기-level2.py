from itertools import permutations #순열
def primeCheck(n) :
  if n < 2 :
    return False
  
  i = 2
  while i*i <= n :
    if n % i == 0 :
      return False
    i+=1
  
  return True

def solution(numbers):
    answer = 0

    numbers = list(map(str,numbers))

    b =[]
    for j in range(1,len(numbers)+1) :
      for i in list(permutations(numbers, j)): #4P2
          b.append(int(''.join(i)))
    b = list(set(b))

    for x in b :
      if primeCheck(x) == True :
        answer += 1

    return answer

print(solution('011'))

