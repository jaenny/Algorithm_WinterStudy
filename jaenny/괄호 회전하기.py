def solution(s):
    answer = 0

    for i in range(len(s)) :
      # 괄호 회전
      temp = s[i:len(s)]+s[0:i]

      # 짝이 맞는 괄호 문자열인지 확인
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