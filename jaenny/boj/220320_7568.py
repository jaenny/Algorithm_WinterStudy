n = int(input())
people = []
for _ in range(n) :
  x,y = map(int,input().split())
  people.append([x,y])

rank = []

for p1 in people :
  cnt = 0
  for p2 in people :
    if p1 == p2 : continue

    if p1[0] < p2[0] and p1[1] < p2[1] :
      cnt += 1
  
  rank.append(cnt + 1)

print(' '.join(map(str,rank)))