def solution(n):
    numbers = [False]*(n+1)
    numbers[0] = numbers[1] = True

    for i in range(2,n+1) :
      if numbers[i] == False :
        j = i+i
        while j <= n :
          numbers[j] = True # 소수 아님
          j += i
    
    answer = 0
    for num in numbers :
        if num == False :
            answer += 1
    return answer
            