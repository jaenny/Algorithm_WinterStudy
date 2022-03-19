# 정답
def solution(goods):
  answer = []

  for good in goods :
    temp = []
    for i in range(1,len(good)+1) : # 개수
      if len(temp) > 0 : break
      for j in range(len(good)) : # 시작위치
        if j+i > len(good) : break
        check = good[j:j+i]
        flag = True
        for other in goods :
          if other == good : continue
          if check in other : # 만약 다른 문자열 안에 찾으려는 문자가 있다면
            flag = False
            break
        if flag :
          temp.append(check)

    if len(temp) > 0 :
      temp = list(set(temp))
      temp.sort()
      answer.append(' '.join(temp))
    else :
      answer.append('None')

  return answer

# print(solution(["pencil","cilicon","contrabase","picturelist"]))
# print(solution(["abcdeabcd","cdabe","abce","bcdeab"]))
print(solution(["ab","ba"]))