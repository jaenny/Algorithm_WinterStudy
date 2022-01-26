def solution(n):
    answer = []
    
    for s in str(n)  :
        answer.append(s)
    answer.sort(reverse=True)
    return int(''.join(answer))