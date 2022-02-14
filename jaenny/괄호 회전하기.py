def solution(s):
    answer = 0

    for i in range(len(s)) :
      temp = s[i:len(s)]+s[0:i]
      if check(temp) :
        answer += 1
      
    return answer

def check(s) :
    stack = []
    
    for bracket in s:
        if len(stack) == 0 :
            stack.append(bracket)
        else :
            top = stack.pop()
            if (top == '[' and bracket == ']') or (top == '{' and bracket == '}') or (top == '(' and bracket == ')'):
                continue 
            else :
              stack.append(top)
              stack.append(bracket)

    if len(stack) > 0 :
        return False
    return True