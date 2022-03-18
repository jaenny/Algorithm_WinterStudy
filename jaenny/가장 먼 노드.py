from collections import deque
def solution(n, edge):
  visit = [-1]*(n+1) # 방문하지 않은 노드의 초기값을 -1로 설정
  visit[1] = 0 # 1번 노드는 0번만에 방문 가능

  vertex = dict() # 간선으로 이어진 노드 정보를 사전에 저장

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
      for n in vertex[node] : # 현재 노드에서 간선으로 이어진 노드 중
        if visit[n] == -1 : # 아직 방문하지 않은 노드가 있다면
          visit[n] = cnt + 1 # 현재 노드까지의 간선 길이 + 1
          queue.append(n)
  
  bfs(queue)

  return visit.count(max(visit))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))