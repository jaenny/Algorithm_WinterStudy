from collections import deque
def solution(n, edge):
  answer = 0

  visit = [-1]*(n+1)
  visit[1] = 0

  vertex = dict()
  for eg in edge :
    a,b = eg
    if a in vertex : vertex[a].append(b)
    else : vertex[a] = [b]
    if b in vertex : vertex[b].append(a)
    else : vertex[b] = [a]

  queue = deque()
  queue.append(1)

  def bfs(queue) :
    while queue :
      node = queue.popleft()
      cnt = visit[node]
      for n in vertex[node] :
        if visit[n] == -1 :
          visit[n] = cnt + 1
          queue.append(n)
  
  bfs(queue)

  return visit.count(max(visit))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))