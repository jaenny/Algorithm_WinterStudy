def right(w) : # 올바른 괄호 문자열인지 판단
  stack = []

  for b in w :
    if len(stack) == 0 :
      stack.append(b)
    else :
      if stack[-1] == '(' and b == ')' :
        stack.pop()
      else :
        stack.append(b)
  return True if len(stack) == 0 else False


def check(w) :
  if w == '' : return ''

  u = ''
  v = ''
  leftCount = 0 # '(' 개수
  rightCount = 0  # ')' 개수
  for i in range(len(w)) :
    if w[i] == '(' : leftCount += 1
    else : rightCount += 1

    if leftCount == rightCount :
      u = w[:i+1]
      v = w[i+1:]
      break

  if right(u) : # u가 올바른 괄호 문자열이라면
    u += check(v)
    return u
  else : # u가 올바른 괄호 문자열이 아니라면
    res = '(' + check(v) + ')'

    new_u = u[1:-1]
    new_u = new_u.replace('(','a')
    new_u = new_u.replace(')', '(')
    new_u = new_u.replace('a', ')')

    return res+new_u

def solution(p) :
  return check(p)

print(solution("()))((()"))