def solution(numbers):
    answer = []
    
    for n in numbers :
        n = int(n) # 이 줄을 추가해야 CASE 7~9 통과
        if n % 2 == 0 or n % 4 == 1:
          answer.append(n+1)
        else :
          k = len(bin(n^(n+1))[2:])
          answer.append(n+2**(k-1)-2**(k-2))

    return answer

print(solution([2,7,11]))
