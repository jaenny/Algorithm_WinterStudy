def solution(n, k, commands):
  cur = k
  table = {i : [i-1, i+1] for i in range(n)}
  answer = ['O']*n
  table[0] = [None, 1]
  table[n-1] = [n-2, None]
  stack = [] # 삭제한 key 저장

  for cmd in commands :
    if cmd == 'C' : # 삭제
      answer[cur] = 'X'
      prev, next = table[cur]

      stack.append([prev,cur,next])
      if next == None : # 맨 마지막 행을 삭제했다면
        cur = prev
      else : cur = next

      # prev, next 다시 이어주기
      if prev == None :
        table[next][0] = None
      elif next == None : 
        table[prev][1] = None
      else :
        table[prev][1] = next
        table[next][0] = prev
    
    elif cmd == 'Z' : # 복구
      prev, now, next = stack.pop()
      answer[now] = 'O'

      if prev == None :
        table[next][0] = now
      elif next == None :
        table[prev][1] = now
      else :
        table[prev][1] = now
        table[next][0] = now
    
    else :
      # 현재 위치 이동
      c, x = cmd.split()
      x = int(x)

      if c == 'D' :
        for _ in range(x) :
          cur = table[cur][1]
      else :
        for _ in range(x) :
          cur = table[cur][0]
  
  return ''.join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))