from collections import defaultdict, deque
from math import inf

N, Q = map(int, input().split())
dic = defaultdict(list)

for _ in range(N-1) :
  p, q, r = map(int, input().split())
  dic[p].append([q,r])
  dic[q].append([p,r])

def findVideo(startVideo, k) :
  queue = deque()
  queue.append([startVideo, inf])
  visit = [0]*(N+1)
  visit[startVideo] = 1

  cnt = 0

  while queue :
    video, dist = queue.popleft()

    for newVideo, newDist in dic[video] :
      if visit[newVideo] : continue # 이미 방문했다면 pass
      visit[newVideo] = 1
      if newDist < dist :
        queue.append([newVideo, newDist])
        if newDist >= k : cnt += 1
      else :
        queue.append([newVideo, dist])
        if dist >= k : cnt += 1
  
  return cnt


for _ in range(Q) :
  k, v = map(int, input().split())
  print(findVideo(v,k))