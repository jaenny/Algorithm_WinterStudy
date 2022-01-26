def GCD(a,b) :
  if b == 0 : return a
  else : return GCD(b,a%b)

def LCM(a,b) :
  return a*b/GCD(a,b)

def solution(n, m):
    answer=[]
    
    answer.append(GCD(n,m))
    answer.append(LCM(n,m))
    return answer

