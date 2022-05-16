def solution(s):
  answer = s
  for i in range(1,len(s)+1) : # 자르는 단위
    new = ''
    cnt = 1
    prev = s[:i]
    for j in range(i,len(s)+1,i) :
      if prev != s[j : j+i] :
        if cnt > 1 : new += str(cnt)+prev
        else : new += prev
        cnt = 1
        prev = s[j : j+i]
      else :
        cnt += 1
    if len(s)%i > 0 :
      new += s[-(len(s)%i):]

    if len(new) < len(answer) : answer = new
  return len(answer)

print(solution('abcabcdede'))