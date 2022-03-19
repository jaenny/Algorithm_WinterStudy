def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9) :
      allCase = set()
      check_number = int((str(N)*i))
      allCase.add(check_number)

      for j in range(0,i-1) :
        for op1 in dp[j] :
          for op2 in dp[-j-1] :
            allCase.add(op1-op2)
            allCase.add(op1+op2)
            allCase.add(op1*op2)
            if op2 != 0 :
              allCase.add(op1//op2)
            print(allCase)
      
      if number in allCase : 
        answer = i
        break

      dp.append(allCase)
    return answer

print(solution(2, 11))