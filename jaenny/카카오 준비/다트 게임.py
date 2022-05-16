def solution(dartResult):
  answer = [0]*len(dartResult)

  i = 0
  j = 0
  while True :
    if dartResult[i].isdecimal() :
      if i+1 < len(dartResult) and dartResult[i+1].isdecimal() :
        num = int(dartResult[i:i+2])
        i += 2
      else :
        num = int(dartResult[i])
        i += 1

    op = dartResult[i]
    if op == 'D' : num = num**2
    elif op == 'T' : num = num **3
    i += 1

    if i >= len(dartResult) : 
      answer[j] = num
      break
    
    if dartResult[i] == '*' :
      num = num * 2
      i += 1
      if j > 0 : answer[j-1] *= 2
    elif dartResult[i] == '#' :
      num *= (-1)
      i += 1
    
    answer[j] = num
    j += 1

    if i >= len(dartResult) : 
      break

  return sum(answer)

print(solution('1D2S3T*'))