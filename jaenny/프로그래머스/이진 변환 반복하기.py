def solution(s):
  cnt = 0 # 회차
  zero = 0 # 제거하는 0의 개수

  while True :
    if s == '1' :
      return [cnt, zero]
    answer = ''

    for c in s :
      if c == '0' : 
        zero += 1
      else :
        answer += c
    
    s = bin(len(answer))[2:]
    cnt += 1

print(solution("1111111"))