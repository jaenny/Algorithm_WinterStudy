def solution(s):
  answer = []
  s = s[2:-2].split('},{')
  s.sort(key = lambda x : len(x))
  
  for ss in s :
    ss = ss.split(',')
    
    if len(ss) == 1 : answer.append(int(ss[0]))
    else :
      for num in ss :
        if int(num) not in answer :
          answer.append(int(num))

  return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))