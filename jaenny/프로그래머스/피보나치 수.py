def solution(n):
  answer = 0

  def Fibo(n) :
    if n == 0 : return 0
    elif n == 1 : return 1
    else :
      return Fibo(n-1) + Fibo(n-2)
  
  return Fibo(n)%1234567

def solution(n):
  answer = 0
  dp = [0]*100001
  dp[1] = 1
  for i in range(2,n+1) :
    dp[i] = dp[i-1]+dp[i-2]
  
  return dp[n]%1234567


print(solution(5))