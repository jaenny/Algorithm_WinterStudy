def solution(brown, yellow):
    answer = []
    cases = [[x,yellow//x] for x in range(1, int((yellow+1)**(1/2))+1) if yellow % x == 0]

    for case in cases :
      if case[0]*2 + case[1]*2 + 4 == brown :
        return [case[1]+2, (brown+yellow) // (case[1]+2)]


print(solution(10,2))
print(solution(8,1))
print(solution(24,24))
print(solution(14,4))
print(solution(18,6))