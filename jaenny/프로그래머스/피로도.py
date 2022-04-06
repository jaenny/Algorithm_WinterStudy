from itertools import permutations

def solution(k, dungeons):
    perm = [x for x in permutations(dungeons, len(dungeons))]
    
    answer = 0

    for p in perm :
        temp = k
        temp_ans = 0
        for dg in p :
            if temp < dg[0] : # 현재 피로도가 최소 필요 피로도보다 작다면
                break
            else :
                temp -= dg[1]
                temp_ans += 1
        answer = max(answer, temp_ans)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))