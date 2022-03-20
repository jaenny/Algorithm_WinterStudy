n = int(input())

end = 1
cnt = 1
for i in range(1,n+1) :
  if i == n :
    print(cnt)
    break
  if end == i :
    end += 6*cnt
    cnt += 1
  