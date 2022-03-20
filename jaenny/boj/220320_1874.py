n = int(input())

per = [] # 입력된 수열
for _ in range(n) :
  per.append(int(input()))

perIndex = 0

num = 2
stack = [1]
res = ['+']
targetIndex = 0
flag = True

while True :
  if targetIndex == n : break

  try:
    popNum = stack.pop()

    if popNum == per[targetIndex] :
      targetIndex+=1
      res.append('-')
    elif popNum < per[targetIndex] :
      stack.append(popNum)
      stack.append(num)
      res.append('+')
      num += 1
    else :
      print('NO')
      flag = False
      break
  except :
    stack.append(num)
    res.append('+')
    num += 1

if flag :
  for r in res :
    print(r)

