def solution(survey, choices):
  answer = ''

  dic = dict()

  for key in ['R','T','C','F','J','M','A','N'] :
    dic[key] = 0

  for i in range(len(survey)) :
    s = survey[i]
    choice = choices[i]
    a, b = s[0], s[1]

    if choice <= 3 :
      if choice == 3 : dic[a] += 1
      elif choice == 1 : dic[a] += 3
      else : dic[a] += 2
    elif choice == 4 : continue
    else :
      dic[b] += choice - 4

  # 1번 지표
  if dic['R'] >= dic['T'] : answer += 'R'
  else: answer += 'T'
  # 2번 지표
  if dic['C'] >= dic['F'] : answer += 'C'
  else: answer += 'F'
  # 3번 지표
  if dic['J'] >= dic['M'] : answer += 'J'
  else: answer += 'M'
  # 1번 지표
  if dic['A'] >= dic['N'] : answer += 'A'
  else: answer += 'N'

  return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))