import sys
m = int(input())

res = set()

for _ in range(m) :
  new = sys.stdin.readline().split()
  op = new[0]
  if len(new) > 1 : x = int(new[1])

  if op == 'add' and x not in res :
    res.add(x)
  elif op == 'remove' and x in res:
    res.remove(x)
  elif op == 'check' :
    if x in res : print(1)
    else : print(0)
  elif op == 'toggle' :
    if x in res :
      res.remove(x)
    else :
      res.add(x)
  elif op == 'all' :
    res = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
  else :
    res = set()