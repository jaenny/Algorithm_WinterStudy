from math import inf
def solution(line):
  star = []

  minX = inf
  maxX = -inf
  minY = inf
  maxY = -inf

  for i in range(len(line)) :
    for j in range(i+1, len(line)) :
      first = line[i]
      second = line[j]

      a, b, e = first
      c, d, f = second

      deno = a*d - b*c
      if deno == 0 : # 두 직선이 평행 또는 일치
        continue
      
      x = (b*f - e*d)/deno
      y = (e*c - a*f)/deno

      # 교점이 정수인 경우만 별 표시
      if x != int(x) or y != int(y) :
        continue

      x = int(x)
      y = int(y)

      # 별이 그려진 최소 사각형을 그리기 위해 x,y의 최소,최대 확인
      minX = min(x, minX)
      maxX = max(x, maxX)
      minY = min(y, minY)
      maxY = max(y, maxY)

      star.append([x,y])
  
  width = maxX - minX
  height = maxY - minY

  matrix = [['.']*(width+1) for _ in range(height+1)]

  # star 찍기
  for s in star :
    i = maxY - s[1]
    j = s[0] - minX
    matrix[i][j] = '*'
  
  for k in range(len(matrix)) :
    matrix[k] = ''.join(matrix[k])

  return matrix

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))