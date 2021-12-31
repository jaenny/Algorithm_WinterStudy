def solution(lottos, win_nums):
    answer = []

    # 최고 순위
    sameNum = 0
    for i in range(len(lottos)) :
      if lottos[i] == 0 :
        sameNum +=1
      elif lottos[i] in win_nums :
        sameNum +=1
    maxRank = 7-sameNum
    if maxRank == 7 : maxRank = 6
    answer.append(maxRank)

    # 최저 순위
    sameNum = 0
    for i in range(len(lottos)) :
      if lottos[i] in win_nums :
        sameNum +=1

    minRank = 7-sameNum
    if minRank == 7 : minRank = 6
    answer.append(minRank)

    return answer


print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))