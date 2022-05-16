a = [1,3,5,7,9,13,15]
b = [4,5,6,8,13]
c = [5,8,13,19]

aIdx = 0
bIdx = 0
cIdx = 0

res = []

while aIdx < len(a) and bIdx < len(b) and cIdx < len(c) :
  if a[aIdx] == b[bIdx] and b[bIdx] == c[cIdx] and a[aIdx] == c[cIdx] :
    res.append(a[aIdx])
    aIdx += 1
    bIdx += 1
    cIdx += 1
  else :
    _max = max(a[aIdx], b[bIdx], c[cIdx])

    if _max > a[aIdx] : aIdx += 1
    if _max > b[bIdx] : bIdx += 1
    if _max > c[cIdx] : cIdx += 1

print(res)
  