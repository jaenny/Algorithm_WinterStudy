import math
from itertools import combinations
n, m = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

chicken = []
house = []

for i in range(n) :
  for j in range(n) :
    if matrix[i][j] == 2 :
      chicken.append([i,j])
    elif matrix[i][j] == 1 :
      house.append([i,j])

res = math.inf
for case in combinations(chicken, m) :
  city = 0
  for h in house :
    houseChicken = math.inf
    for c in case :
      houseChicken = min(houseChicken, abs(h[0]-c[0])+abs(h[1]-c[1]))
    city += houseChicken
  res = min(res, city)
print(res)
