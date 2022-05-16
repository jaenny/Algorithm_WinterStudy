from collections import defaultdict, deque

isWolf = list()
num2deges = defaultdict(list)
maxSheep = 0

def dfs(cur, used, sheep, wolf, canGo) :
  global maxSheep

  if used[cur] : return # 이미 방문한 경우라면 return
  used[cur] = True

  if isWolf[cur] : wolf += 1
  else :
    sheep += 1
    maxSheep = max(maxSheep, sheep)
  
  if sheep <= wolf : return

  canGo.extend(num2deges[cur])

  for next in canGo :
    nused = used.copy()
    ncanGo = [n for n in canGo if n != next and not used[n]]
    dfs(next, nused, sheep, wolf, ncanGo)



def solution(info, edges) :
  num2deges = defaultdict(list)
  maxSheep = 0

  isWolf = info
  used = [False]*len(isWolf)

  for parent, child in edges :
    num2deges[parent].append(child)
  
  queue = deque()
  queue.append([0,used,0,0,[]])

  while queue :
    cur, used, sheep, wolf, canGo = queue.popleft()

    if used[cur] : continue
    used[cur] = True

    if isWolf[cur] : wolf += 1
    else : sheep += 1

    if wolf >= sheep : continue
    maxSheep = max(maxSheep, sheep)

    canGo.extend(num2deges[cur])

    for next in canGo :
      nused = used.copy()
      ncanGo = [n for n in canGo if n!=next and not used[n]]
      queue.append([next, nused, sheep, wolf, ncanGo])

  return maxSheep


print(solution([0,1,0,1,1,0,1,0,0,1,0], 	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))