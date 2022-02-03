from collections import deque

def solution(priorities, location):
    answer = 0
    
    p = deque(priorities)
    index = deque([x for x in range(len(priorities))])
    
    while True :
        newP = p.popleft()
        newI = index.popleft()

        if len(p) == 0 :
          return answer + 1
        
        if max(list(p)) > newP : # 뒤쪽에 중요도가 더 높은 문서가 있다면 다시 마지막에 추가
            p.append(newP)
            index.append(newI)
        else :
            answer += 1
            if newI == location :
                return answer

print(solution([2,1],1))