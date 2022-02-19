def solution(numbers):
    answer = []
    
    for n in numbers :
        n = int(n) # 이 줄을 추가해야 CASE 7~9 통과
        if n % 2 == 0 :
          answer.append(n+1)
        else :
          if n % 4 == 1 :
            answer.append(n+1)
          else :
            n_bit = bin(n)
            cnt = 0
            for i in range(len(n_bit)-1,-1,-1) :
              if n_bit[i] == '1' :
                cnt += 1
              else :
                break
            y = cnt - 1
            answer.append(n+(2**(cnt - 1)))

    return answer

print(solution([2,7,11]))