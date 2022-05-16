def primeCheck(n) :
  numbers = [False]*(2*n+1)
  numbers[0] = numbers[1] = True

  for i in range(2,2*n+1) :
    if numbers[i] == False :
      j = i+i
      while j <= 2*n :
        numbers[j] = True
        j += i
  
  return numbers[n+1:2*n+1].count(False)

while True :
  n = int(input())
  if n == 0 : break

  print(primeCheck(n))