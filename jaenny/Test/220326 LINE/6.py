import heapq
def solution(req_id, req_info):
  answer = []

  accounts = [[req_id[i], 0, 0] for i in range(len(req_id))] # 이름, 골드, 실버

  buy = []
  sell = []
  for i in range(len(req_info)) :
    reqType, reqAmount, reqPrice = req_info
    if reqType == 0 : # 구매요청
      if len(sell) == 0 : # 판매 대기가 비어있으면 구매 요청도 처리할 수 없음. 바로 대기처리
        heapq.heappush(buy, [-reqPrice, i, reqAmount]) # pending - 가격, 인덱스, 양
      else : # 판매 대기가 있음
        while sell :
          sellPrice, sellIndex, sellAmount = heapq.heappop(sell)
          if sellPrice <= reqPrice : # 팔려는 가격 <= 사려는 가격
            amount = min(sellAmount, reqAmount )

            # 판매자의 계좌에서 구매자의 계좌로 amount 만큼 골드 이동
            accounts[sellIndex][1] += amount
            accounts[i][1] -= amount

            # 구매자의 계좌에서 판매자의 계좌로 amount × sell_price만큼의 실버가 이동
            accounts[sellIndex][2] -= amount*sellPrice
            accounts[i][2] += amount*sellPrice

            req_info[i][2] -= amount
            if node[2] - amount == 0 : 
              sell.remove(node)
              break
            else :
              heapq.heappush(sell, [node[0], node[1], node[2]-amount])
          else :
            
      print(buy)
      for a in accounts :
        print(a)
      print()
    elif reqType == 1 : # 판매요청
      if len(buy) == 0 : # 구매요청이 없으면
        heapq.heappush(sell, [req_info[i][1], i, req_info[i][2]]) # pending


  

  
  return answer

print(solution(["Morgan", "Teo", "Covy", "Covy", "Felix"], [[0, 10, 50], [1, 35, 70], [0, 10, 30], [0, 10, 50], [1, 11, 40]]))