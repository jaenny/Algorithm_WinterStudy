n = int(input()) # 지방의 수
cities = list(map(int,input().split()))
budget = int(input())
sumCity = sum(cities)
start = 0
end = 1000000000
answer = 0
if sumCity <= budget : 
  print(max(cities))
else :
  while start <= end :
    mid = (start + end) // 2 # 상한액
    total = 0
    for city in cities :
      if mid <= city : total += mid
      else : total += city
      
    if total > budget :
      end = mid - 1
    else :
      start = mid + 1
      answer = max(answer, mid)

  print(answer)