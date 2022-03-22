def solution(arr):
  answer = []

  def quad_tree(x,y,n) :
    color = arr[x][y]

    for i in range(x, x+n) :
      for j in range(y, y+n) :
        if color != arr[i][j] :
          quad_tree(x, y, n//2)
          quad_tree(x, y+n//2, n//2)
          quad_tree(x+n//2, y, n//2)
          quad_tree(x+n//2, y+n//2, n//2)
          return
    answer.append(color)
    # print(answer)

  quad_tree(0, 0, len(arr))
  return [answer.count(0),answer.count(1)]

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]

res = solution(matrix)
print(res[0])
print(res[1])