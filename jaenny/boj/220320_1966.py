from collections import deque
tc = int(input())

for _ in range(tc) :
  n, target = list(map(int,input().split()))
  priority = list(map(int,input().split()))
  priority = [[i,priority[i]] for i in range(n)]

  cnt = 1
  priority = deque(priority)
  
  while priority :
    left = priority.popleft()
    importance = left[1]
    flag = True

    for x in priority :
      if importance < x[1] :
        # 뒤에 중요도가 더 높은 문서가 있다면
        priority.append(left) # 뒤로 추가
        flag = False
        break
    
    if flag : # 뒤에 중요도가 더 높은 문서가 없어서 출력되는데
      if left[0] == target : # 몇 번째로 출력되는지 궁금했던 문서라면
        print(cnt) # 몇 번째인지 출력
        break
      else : # 아니라면 출력된 횟수 + 1
        cnt += 1