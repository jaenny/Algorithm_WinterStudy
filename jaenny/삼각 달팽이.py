def solution(n):
  answer = []
  matrix = [[0]*n for _ in range(n)]

  cnt = n
  nums = [[] for _ in range(n)]
  before = 0
  i = 0
  for num in range(1, sum(range(1,n+1))+1) :
    nums[i].append(num)
    if before + cnt == num :
      before = num
      i += 1
      cnt -= 1
  # n = 4 일 경우
  # nums = [[1,2,3,4], [5,6,7], [8,9], [10]] -> 방향이 같은 수들끼리 한 배열로 묶임

  dr = [0,1,2] # 아래쪽, 오른쪽, 왼쪽위
  y = x = 0 # matrix에서 사용할 좌표

  for i in range(len(nums)) :
    d = dr[i%3] # 방향 정하기

    if d == 0 : # 아래쪽
      for j in range(len(nums[i])) :
        matrix[y][x] = nums[i][j]
        y += 1
        if j == len(nums[i])-1 : # 마지막에 닿으면 오른쪽 방향으로 좌표 준비
          y -= 1
          x += 1
    elif d == 1 : # 오른쪽
      for j in range(len(nums[i])) :
        matrix[y][x] = nums[i][j]
        x += 1
        if j == len(nums[i])-1 : # 마지막에 닿으면 왼쪽위 방향으로 좌표 준비
          y -= 1
          x -= 2
    else :
      for j in range(len(nums[i])) :
        matrix[y][x] = nums[i][j]
        y -= 1
        x -= 1
        if j == len(nums[i])-1 : # 마지막에 닿으면 아래쪽 방향으로 좌표 준비
          y += 2
          x += 1
    
  for col in matrix :
    for num in col :
      if num == 0 :
        break
      answer.append(num)

  return answer