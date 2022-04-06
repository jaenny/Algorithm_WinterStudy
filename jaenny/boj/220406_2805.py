n, m = map(int,input().split())

trees = list(map(int,input().split()))

start = 0
end = 1000000000
answer = 0

while start <= end :
  mid = (start + end) // 2
  res = 0

  for tree in trees :
    if tree > mid :
      res += tree - mid

  if m <= res :
    start = mid + 1
    answer = max(answer, mid)
  else :
    end = mid - 1

print(answer)
