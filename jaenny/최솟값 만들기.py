# from itertools import permutations
# from math import inf
# def solution(A,B):
#   answer = inf

#   multiples = [[0]*len(A) for _ in range(len(A))]

#   for i in range(len(A)) :
#     for j in range(len(A)) :
#       multiples[i][j] = A[i]*B[j]
  
#   # for m in multiples :
#   #   print(m)

#   cases = [x for x in permutations(range(len(A)))]

#   for case in cases :
#     temp = 0
#     for i in range(len(A)) :
#       temp += multiples[i][case[i]]
#     answer = min(answer, temp)

#   return answer

def solution(A,B) :
  A.sort()
  B.sort(reverse=True)

  answer = 0
  for i in range(len(A)) :
    answer += A[i]*B[i]
  return answer


print(solution([1,4,2], [5,4,4]))