def solution(sentences, n):
  answer = 0

  def check(alpha, sentence) :
    t = 0
    for al in sentence :
      if al == ' ' : t+=1
      elif al.isupper() :
        if 'shift' in alpha and al.lower() in alpha: 
          t += 2
        else : 
          return 0
      else :
        if al in alpha :
          t += 1
        else : 
          return 0
    return t


  for sentence in sentences :
    alpha = []
    for c in sentence :
      if c.isupper() and 'shift' not in alpha:
        alpha.append('shift')
        alpha.append(c.lower())
      elif c.isupper() :
        alpha.append(c.lower())
      elif c.islower() and c not in alpha :
        alpha.append(c)
    
    if len(alpha) > n : continue
    
    temp = 0
    for sent in sentences :
      r = check(alpha, sent)
      # print("r",r)
      temp += r
    # print(temp)
    # print()
    
    answer = max(answer, temp)
  return answer

print(solution(["line in line", "LINE", "in lion"], 5))
print(solution(["ABcD", "bdbc", "a", "Line neWs"], 7))