import heapq
from collections import deque
def solution(arr, processes):
  answer = [0]*len(processes)

  now, i,use = 0, 0, 0
  start = -1
  heap = []

  wait = [] # 대기중
  work = deque() # 작업중

  while i < len(processes) :
    temp = []
    for q in range(len(processes)) :
      pro = processes[q].split()
      if start < int(pro[1]) <= now :
        # now초에 작업을 시작하는 것들 고르기
        if pro[0] == 'write' : # write = 0
          heapq.heappush(temp, [0,int(pro[1]),int(pro[1])+int(pro[2])-1,1,int(pro[2]),int(pro[3]),int(pro[4]),pro[5],q])
        else :
          heapq.heappush(temp, [1,int(pro[1]),int(pro[1])+int(pro[2])-1,1,int(pro[2]),int(pro[3]),int(pro[4]),q])

    for t in temp :
      # 현재 작업중인게 없음
      if len(work) == 0 :
        work.append(t)
      # 현재 읽기 작업중
      elif work[0][0] == 1 :
        if t[0] == 1 : # 새로운 작업이 읽기라면
          if len(wait) > 0 and wait[0][0] == 0 : # 그런데 대기에 쓰기가 기다린다면 읽기도 대기열로
            heapq.heappush(wait, t)
          else :
            t[3] = 1
            work.append(t)
        else :
          heapq.heappush(wait, t)
      # 현재 쓰기 작업중
      elif work[0][0] == 0 :
        heapq.heappush(wait, t)

    # wait에 있는 작업들 work로 옮기기
    print(now,"wait",wait)
    for w in range(len(wait)) :
      if len(work) == 0 :
        move = heapq.heappop(wait)
        move[3] = 1
        work.append(move)
      elif work[0][0] == 1 :
        move = heapq.heappop(wait)
        if move[0] == 1 :
          move[3] = 1
          work.append(move)
        else :
          heapq.heappush(wait,move)
      elif work[0][0] == 0 :
        break

    # now초에 작업중
    j = 0
    idx = 0
    print(now, "work",work)
    if len(work) > 0 : use += 1
    while j < len(work) :
      w = work[j]
      # print(j,w)
      if w[0] == 1 and w[4] ==w[3] :
        if w[0] == 1 :
          print(arr)
          # 읽기 작업
          answer[w[-1]] = ''.join(arr[w[5]:w[6]+1])
        work[j][0] = 2
        i += 1
      elif w[0] == 0 and w[3] == w[4] :
        for a in range(w[5],w[6]+1) :
          arr[a] = w[7]
        answer[w[-1]] = ''
        work[j][0] = 2
        i += 1
      else :
        work[j][3] += 1
        idx+= 1
      j += 1
    # print(work)

    k = 0
    while k < len(work) :
      if work[k][0] == 2 : work.popleft()
      else : break 


    print(answer)

    now += 1
    start += 1
    print(use)
    print()
  answer = [x for x in answer if x != '']
  answer.append(str(use))
  return answer

print(solution(["1","2","4","3","3","4","1","5"], ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]))
# print(solution(["1","1","1","1","1","1","1"], ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]))