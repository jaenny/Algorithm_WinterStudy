from math import inf
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

matrix = [[inf]*n for _ in range(n)]

for _ in range(m) :
  a,b = map(int,input().split())
  matrix[a-1][b-1] = 1
  matrix[b-1][a-1] = 1

for k in range(n) :
  for i in range(n) :
    for j in range(n) :
      matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

# print(matrix)

res = inf
person = inf

for f in range(n) :
  # print(f, sum(matrix[f])-matrix[f][f])
  if res > sum(matrix[f])-matrix[f][f] :
    res = sum(matrix[f])-matrix[f][f]
    person = f
  elif res == sum(matrix[f])-matrix[f][f] and person > f :
    person = f
print(person+1)