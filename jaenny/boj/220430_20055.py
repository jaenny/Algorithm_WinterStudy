from collections import deque
n, k = map(int,input().split())

belt = deque(list(map(int, input().split())))
for i in range(len(belt)) :
  belt[i] = [belt[i], False]

cnt = 1
while True :
  # print('-----------')
  # print(belt)
  # 회전
  last = belt.pop()
  belt.appendleft(last)
  # print('회전 이후', belt)

  # 내리기
  if belt[n-1][1] == True :
    belt[n-1][1] = False
  # print('내리기',belt)
  
  # 로봇 이동
  for i in range(n-1,-1,-1) :
    if belt[i][1] == True and belt[i+1][0] > 0 and belt[i+1][1] == False :
      belt[i][1] = False
      belt[i+1][0] -= 1
      belt[i+1][1] = True
  # print('로봇 이동', belt)

  # 내리기
  if belt[n-1][1] == True :
    belt[n-1][1] = False
  # print('내리기',belt)
  
  # 올리기
  if belt[0][0] > 0 and belt[0][1] == False :
    belt[0][0] -= 1
    belt[0][1] = True
  # print('올리기', belt)
  
  # 전체 내구도 체크
  temp = 0
  flag = 0
  for i in range(len(belt)) :
    if belt[i][0] == 0 :
      temp += 1
      if temp >= k : 
        print(cnt)
        flag = 1
        break
  if flag == 1 :
    break
  else : cnt += 1
