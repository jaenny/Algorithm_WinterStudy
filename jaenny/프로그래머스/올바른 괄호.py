def solution(st):
  stack = []
  for s in st :
    if len(stack) == 0 : stack.append(s)
    else :
      temp = stack.pop()
      if temp == '(' and s == ')' :
        continue
      else :
        stack.append(temp)
        stack.append(s)
  
  if len(stack) == 0 : return True
  else : return False 
