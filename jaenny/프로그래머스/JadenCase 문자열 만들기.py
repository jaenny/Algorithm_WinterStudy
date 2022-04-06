def solution(s):
  s = list(map(str, s))

  for i in range(len(s)) :
    if s[i] == ' ' or s[i].isdigit(): continue

    if i==0 or s[i-1]==' ' : 
      s[i] = s[i].upper()
    else :
      s[i] = s[i].lower()

  return ''.join(s)

print(solution("3fOr the  last week"))