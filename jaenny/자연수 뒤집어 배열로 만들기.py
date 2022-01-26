def solution(n):
    answer = []
    for s in str(n) :
        answer.append(int(s))
    
    answer.reverse()
    return answer