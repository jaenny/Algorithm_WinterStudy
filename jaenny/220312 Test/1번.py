def solution(money, costs):
  answer = 0
  coins = [500,100,50,10,5,1]
  count = [0,0,0,0,0,0] # 각 동전을 최소로 사용했을 때 개수
  # 500원 개수, 100원 개수 ... 순서

  res = [0,0,0,0,0,0]
  costs.reverse()

  for i in range(6) :
    count[i] = money // coins[i]
    money = money % coins[i]

  for j in range(6) :
    temp = count[j] * coins[j]
    res[j] = count[j] * costs[j]
    # print(temp, res[j])
    for k in range(j+1, 6) :
      if j == k : continue
      # print( costs[k] , (temp // coins[k]), costs[k] * (temp // coins[k]))
      res[j] = min(res[j], costs[k] * (temp // coins[k]))
    # print(res)

  return sum(res)

print(solution(4578, 	[1, 4, 99, 35, 50, 1000]))
print(solution(1999, 	[2, 11, 20, 100, 200, 600]))