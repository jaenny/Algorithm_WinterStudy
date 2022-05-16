tc = int(input())

for _ in range(tc) :
  n = int(input())
  cloth = dict()
  res = 1
  for _ in range(n) :
    name, category = input().split()

    if category in cloth :
      cloth[category].append(name)
    else :
      cloth[category] = [name]
  
  for cl in cloth.keys() :
    res *= len(cloth[cl])+1
  
  if n == 0 :
    print(0)
  else :
    print(res-1)