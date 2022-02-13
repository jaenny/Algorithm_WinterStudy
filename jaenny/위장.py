def solution(clothes):
    answer = 0

    # 해시 만들기
    closet = dict()

    for cloth in clothes :
      if cloth[1] not in closet :
        closet[cloth[1]] = [cloth[0]]
      else :
        closet[cloth[1]].append(cloth[0])

    

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))