def solution(s):
  if len(s) % 2 == 1 : return 0 # 문자열 길이가 홀수면 바로 실패

  stack = [s[0]]

  for c in s[1:] :
    if len(stack) > 0 and stack[-1] == c :
      stack.pop()
    else :
      stack.append(c)
  
  return 0 if len(stack) > 0 else 1


print(solution('baabaa'))
print(solution('cdcd'))