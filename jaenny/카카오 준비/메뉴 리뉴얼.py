from itertools import combinations
import heapq

def solution(orders, course):
  answer = []

  for c in course :
    temp = []
    menus = set() # 고를 수 있는 메뉴들 저장
    for order in orders :
      for comb in combinations(sorted(order), c) :
        menus.add(comb)

    for menu in menus :
      cnt = 0
      for order in orders :
        if set(menu) - set(order) == set() :
          cnt += 1
      if cnt > 1 :
        heapq.heappush(temp, [-cnt,''.join(menu)])
    
    if len(temp) > 0 :
      _max = temp[0][0]
      while temp :
        cnt, menu = heapq.heappop(temp)
        if cnt == _max :
          answer.append(menu)
        else : 
          break
    
  answer.sort()
  return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
