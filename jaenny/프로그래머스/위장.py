def solution(clothes):
    answer = 1

    # 해시 만들기
    closet = dict()

    for cloth in clothes :
      if cloth[1] not in closet :
        closet[cloth[1]] = [cloth[0]]
      else :
        closet[cloth[1]].append(cloth[0])
    
    for key in closet.keys() :
      answer *= (len(closet[key])+1)
    
    return answer -1

    

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))