def solution(n):
    if n % 2 == 1 :
        return 2
    
    return primeCheck(n-1)

def primeCheck(n) :
  if n < 2 :
    return False
  
  i = 2
  while i<= n :
    if n % i == 0 :
      return i
    i+=1  
  return True