n, m = map(int,input().split())

memo = dict()
for _ in range(n) :
  site, pw = map(str, input().split())
  memo[site] = pw

for _ in range(m) :
  print(memo[input()])
