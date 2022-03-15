from math import inf
from itertools import permutations
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

res = inf

def check(cost) :
  for i in range(n) :
    if matrix[case[i]][case[i+1]] == 0 :
      return False
    cost += matrix[case[i]][case[i+1]]
  return cost

for case in permutations(range(n)) :
  case = list(case) + [case[0]]
  cost = check(0)
  if cost :
    res = min(cost, res)
print(res)