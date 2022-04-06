def solution(s, n):
    answer = ''
    
    for c in s :
      isBig = False
      if c == ' ' :
        answer += ' '
        continue
      c = ord(c)
      if c <= 90 : 
        isBig = True
      c += n
      if isBig == True and c >= 91 :
        c -= 26
      elif isBig == False and c >= 123 :
        c -= 26
      c = chr(c)

      answer += c
    return answer