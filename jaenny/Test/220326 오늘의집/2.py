from math import inf
def solution(beds, tables, cost) :
  minCost = inf
  for bed in beds :
    for table in tables :
      a,b,c,d = bed[0], bed[1], table[0], table[1]
      case1 = (a+d)*max(b,c)
      case2 = (b+d)*max(a,c)
      case3 = (b+c)*max(a,d)
      case4 = (a+c)*max(b,d)
      minCost = min(minCost, bed[2]+table[2]+min(case1, case2, case3, case4)*cost)

  return minCost

print(solution([[4, 1, 200000]],[[2, 3, 100000]], 10000))
print(solution([[2, 3, 40], [2, 5, 20]],[[1, 1, 30]], 10000	))
print(solution([[2, 3, 40000], [2, 5, 20000]]	, [[1, 1, 30000]], 10))