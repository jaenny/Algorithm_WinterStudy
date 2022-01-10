def solution(x, n):
    answer = []
    
    i = x
    count = 1
    while count <= n :
        answer.append(i)
        i+=x
        count += 1
    return answer