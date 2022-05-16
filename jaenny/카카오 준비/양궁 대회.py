from itertools import combinations_with_replacement

def counting(apeach, case) :
  lion = [0,0,0,0,0,0,0,0,0,0,0]
  for c in case :
    lion[c] += 1

  lion.reverse()

  score = [0,0] # 어피치, 라이언
  for i in range(11) :
    if lion[10-i] > apeach[10-i] : score[1] += i
    elif lion[10-i] == apeach[10-i] == 0 : continue
    else : score[0] += i
  
  if score[0] < score[1] : 
    return [score[1]-score[0],lion]
  else : return 'apeach'

def solution(n, info):
  cases = list(combinations_with_replacement([10,9,8,7,6,5,4,3,2,1,0],n))

  maxScore = 0
  maxBoard = [0,0,0,0,0,0,0,0,0,0,0]

  for case in cases :
    res = counting(info, case)
    if res != 'apeach' :
      if maxScore < res[0] :
        maxScore = res[0]
        maxBoard = res[1]
      elif maxScore == res[0] : 
        for i in range(10,-1,-1) :
          if res[1][i] == maxBoard[i] : continue
          elif res[1][i] > maxBoard[i] : 
            maxBoard = res[1]
            break
          else : break


  if maxScore > 0 :
    return maxBoard
  else :
    return [-1]

