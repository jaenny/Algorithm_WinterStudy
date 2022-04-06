def solution(n, computers):
  answer = 0
  visit = [[False]*n for _ in range(n)]
  graph = {x+1:[] for x,y in enumerate(range(n))}
  for i in range(n) :
    for j in range(n) :
      if computers[i][j] == 1 :
        graph[i+1].append(j+1)

  def dfs(y) :
    i = y
    stack = graph[y]
    if len(stack) == 0 : return False
    while stack :
      x = stack.pop()
      if visit[y-1][x-1] == False :
        visit[y-1][x-1] == True
        dfs(x)
    return True

  for i in range(1,n+1) :
    if dfs(i) : 
      answer += 1
        
  return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]		))