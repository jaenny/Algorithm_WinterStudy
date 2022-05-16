from itertools import permutations
def solution(expression):
  ops = [x for x in permutations(['*','+','-'])]
  res = -1

  temp = expression
  temp = temp.replace('-',' - ')
  temp = temp.replace('*',' * ')
  temp = temp.replace('+',' + ')
  expression = temp

  expression = expression.split()
  ori = expression.copy()

  for op in ops :
    expression = ori.copy()
    for o in op :
      new = []
      i = 0
      prev = 0
      while (i < len(expression)) :
        if o == expression[i] :
          new.pop()
          if o == '+' : t = int(prev)+int(expression[i+1])
          elif o == '-' : 
            t = int(prev)-int(expression[i+1])
          else : t = int(prev)*int(expression[i+1])
          new.append(t)
          prev = t
          i += 1
        else :
          new.append(expression[i])
          prev = expression[i]
        i += 1
      expression = new
    res = max(res, abs(expression[0]))

  return res
print(solution("50*6-3*2"))