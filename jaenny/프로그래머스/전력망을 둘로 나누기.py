def solution(n, wires):
  answer = 10000000000000

  maps = dict()
  for num in range(1,n+1) :
    maps[num] = []
  
  for wire in wires :
    maps[wire[0]].append(wire[1])
    maps[wire[1]].append(wire[0])
  
  def bfs(start, visit, cnt) :
    for k in maps[start] :
      if visit[k-1] == False : # 아직 방문 전
        visit[k-1] = True
        cnt = bfs(k, visit, cnt+1)
    return cnt

  for num in range(1, n+1) :
    for dest in maps[num] :
      # num에서 dest를 끊는다면

      # dest에서 이어진 것들 탐색
      visit = [False for _ in range(n)]
      visit[num-1] = True
      visit[dest-1] = True
      from_dest = bfs(dest, visit, 0)

      # num에서 이어진 것들 탐색
      visit = [False for _ in range(n)]
      visit[num-1] = True
      visit[dest-1] = True
      from_num = bfs(num, visit, 0)

      answer = min(answer, abs(from_dest - from_num))

  return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))