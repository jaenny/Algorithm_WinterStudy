def solution(n):
    arr = ['0','1','2','4']
    if n <= 3 :
      return arr[n]
    
    answer = ''
    while n>3 :
      if n % 3 != 0 :
        answer = str(n % 3) + answer
        n = n//3
      else :
        answer = '4' + answer
        n = n//3 - 1

    return arr[n]+answer