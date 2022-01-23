def solution(s):
    answer = sorted(s)
    answer.reverse()
    answer = ''.join(answer)
    return answer