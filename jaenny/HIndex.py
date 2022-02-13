def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    
    h = 0
    while True:
      up = [x for x in citations if x >= h]
      if len(up) >= h : # h번 이상 인용된 논문이 h편 이상이고
        h += 1
      else :
        return h-1

print(solution([3,0,6,1,5]))