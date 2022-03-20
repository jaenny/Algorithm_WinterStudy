n = int(input())

per = [] # 입력된 수열
for _ in range(n) :
  per.append(int(input()))

perIndex = 0 # 입력된 수열의 인덱스

num = 2 # stack에 새로 push될 다음 값
stack = [1] # stack
res = ['+'] # push 했으면 + pop 했으면 -

targetIndex = 0 # pop 완료한 개수
flag = True # 입력된 수열을 만들 수 있는지 여부

while True :
  # 만약 n개의 수를 모두 찾았다면 break
  if targetIndex == n : break

  # 빈 stack에서 pop을 호출하면 에러가 발생하기 때문에
  # try-except 문으로 작성
  try:
    popNum = stack.pop()

    if popNum == per[targetIndex] :
      # 만약 stack의 마지막 수가 구하려는 수와 같다면
      targetIndex+=1
      res.append('-')
    elif popNum < per[targetIndex] :
      # 만약 stack의 마지막 수가 구하려는 수보다 작다면
      stack.append(popNum)
      stack.append(num)
      res.append('+')
      num += 1
    else :
      # 만약 stack의 마지막 수가 구하려는 수보다 크다면
      # 이는 만들 수 없는 수열
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

