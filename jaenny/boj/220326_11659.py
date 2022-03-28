import sys
input = sys.stdin.readline
n, m = map(int,input().split())

nums = list(map(int, input().split()))

_sum = [0]*(n+1)

total = 0
for i in range(1,n+1) :
  total += nums[i-1]
  _sum[i] = total

for _ in range(m) :
  a,b = map(int,input().split())
  print(_sum[b] - _sum[a-1])