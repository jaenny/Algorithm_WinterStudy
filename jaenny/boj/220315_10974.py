from itertools import permutations

n = int(input())

for per in permutations(range(1,n+1)) :
  print(' '.join(map(str,per)))
