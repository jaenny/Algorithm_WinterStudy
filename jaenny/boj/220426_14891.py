from collections import deque
gears = [deque(list(map(int, input()))) for _ in range(4)]

n = int(input())
cases = [list(map(int, input().split())) for _ in range(n)]

def rotate(gearNum, direction) :
  if direction == 1 : # 시계방향
    x = gears[gearNum-1].pop()
    gears[gearNum-1].appendleft(x)
  else :
    x = gears[gearNum-1].popleft()
    gears[gearNum-1].append(x)


for start, d in cases :
  # 1번 톱니바퀴 돌리기
  if start == 1 :
    # 일단 1번 톱니바퀴 부터 돌린다.
    moveNext = gears[0][2] != gears[1][6]
    rotate(start, d)
    # 1-2번 비교
    if moveNext : # 다른 극 -> 회전
      moveNext = gears[1][2] != gears[2][6]
      rotate(2, d*(-1))
      # 2-3번 비교
      if moveNext :
        moveNext = gears[2][2] != gears[3][6]
        rotate(3, d)
        # 3-4번 비교
        if moveNext :
          rotate(4, d*(-1))


  # 2번 톱니바퀴 돌리기
  elif start == 2 :
    moveLeft = gears[0][2] != gears[1][6]
    moveRight = gears[1][2] != gears[2][6]
    rotate(start, d)

    # 1-2번 비교
    if moveLeft :
      rotate(1, (-1)*d)

    # 2-3번 비교
    if moveRight :
      moveRight = gears[2][2] != gears[3][6]
      rotate(3, (-1)*d)
      # 3-4번 비교
      if moveRight :
        rotate(4, d)

  # 3번 톱니바퀴 돌리기
  elif start == 3 :
    moveLeft = gears[1][2] != gears[2][6]
    moveRight = gears[2][2] != gears[3][6]
    rotate(start, d)


    # 2-3번 비교
    if moveLeft :
      moveLeft = gears[0][2] != gears[1][6]
      rotate(2, (-1)*d)
      # 1-2번 비교
      if moveLeft :
        rotate(1, d)

    # 3-4번 비교
    if moveRight :
      rotate(4, (-1)*d)

  # 4번 톱니바퀴 돌리기
  elif start == 4 :
    # 일단 4번 톱니바퀴 부터 돌린다.
    moveLeft = gears[3][6] != gears[2][2]
    rotate(start, d)
    # 4-3번 비교
    if moveLeft :
      moveLeft = gears[2][6] != gears[1][2]
      rotate(3, (-1)*d)
      # 3-2번 비교
      if moveLeft :
        moveLeft = gears[1][6] != gears[0][2]
        rotate(2, d)
        # 2-1번 비교
        if moveLeft :
          rotate(1, d*(-1))

res = 0
if gears[0][0] : res += 1
if gears[1][0] : res += 2
if gears[2][0] : res += 4
if gears[3][0] : res += 8
print(res)