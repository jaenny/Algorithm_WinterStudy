for t in range(1,11) :
  answer = 0
  l = input()
  apartment = list(map(int,input().split()))

  for i in range(2,len(apartment)-2) :
    _max = max(apartment[i-2],apartment[i-1],apartment[i+1],apartment[i+2])

    if apartment[i] > _max :
      answer += apartment[i] - _max

  print('#'+str(t),answer)