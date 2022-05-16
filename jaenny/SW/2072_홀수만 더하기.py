T = int(input())

for t in range(1,T+1) :
  nums = list(map(int,input().split()))

  _sum = sum([num for num in nums if num % 2 != 0])

  print("#%d %d" %(t, _sum))