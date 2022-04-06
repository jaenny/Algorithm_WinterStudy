from itertools import product

def solution(word):
  answer = 0

  sets = ['A','E','I','O','U']

  data = []
  for i in range(1,6) :
    data += list(product(sets, repeat = i))

  data.sort()
  answer = data.index(tuple(word))

  return answer+1


print(solution("AAAE"))