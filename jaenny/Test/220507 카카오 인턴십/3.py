from collections import deque
def solution(alp, cop, problems):
  answer = 0

  req = [0,0]
  for p in problems :
    ra = p[0]
    rc = p[1]
    if req[0] < ra : req[0] = ra
    if req[1] < rc : req[1] = rc

  visit = dict()
  queue = deque()
  queue.append([alp, cop, 0])
  visit[str(alp)+' '+str(cop)] = 0

  cnt = 0
  while queue :
    a, c, time = queue.popleft()
    # print(a,c,time)
    
    if [a,c] == req : return visit[str(a)+' '+str(c)]

    # 알고리즘 공부하기
    if str(a+1)+' '+str(c) not in visit :
      visit[str(a+1)+' '+str(c)] = time + 1
      queue.append([a+1, c, time+1])

    # 코딩력 공부하기
    if str(a)+' '+str(c+1) not in visit :
      visit[str(a)+' '+str(c+1)] = time + 1
      queue.append([a, c+1, time+1])

    # 풀 수 있는 문제 있으면 풀기
    for p in problems :
      ra, rc = p[0], p[1]
      if a >= ra and c >= rc and p[2]+p[3] > p[4]:
        if str(a+p[2])+' '+str(c+p[3]) in visit :
          if visit[str(a+p[2])+' '+str(c+p[3])] > time + p[4] :
            visit[str(a+p[2])+' '+str(c+p[3])] = time+p[4]
            queue.append([a+p[2], c+p[3], time+p[4]])
        else :
          visit[str(a+p[2])+' '+str(c+p[3])] = time+p[4]
          queue.append([a+p[2], c+p[3], time+p[4]])

  return answer

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))