def solution(w,h):
    answer = 0
    if w == h :
      return w*h - w
    i = 1
    prev = 0
    while i != h+1 :
      print(int(i*w/h), i)
      answer += int(i*w/h)
      if prev != int(prev) :
        answer -= 1
      print(answer)
      prev = i*w/h
      i+=1
    return answer*2

print(solution(3,5))