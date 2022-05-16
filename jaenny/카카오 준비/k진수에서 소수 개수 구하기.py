def findnk(n,k) :
  rev_base = ''

  while n > 0:
      n, mod = divmod(n, k)
      rev_base += str(mod)
  return rev_base[::-1]

import math
def isPrime(n) :
  if n < 2 :
    return False
  
  i = 2
  while i*i <= n :
    if n % i == 0 :
      return False
    i += 1
  
  return True

def solution(n, k):
  answer = 0
  
  # k진법으로 바꾸기
  nk = findnk(n, k)
  nk = nk.replace('0', ' ')
  nk = list(map(int, nk.split()))

  for num in nk :
    if isPrime(num) : answer += 1

  return answer
print(solution(437674, 3))