def solution(prices):
    answer = []
    
    for i in range(len(prices)-1) :
        cnt = 0
        for j in range(i+1, len(prices)) :
            if prices[i] <= prices[j] :
                cnt += 1
            else:
                break
        answer.append(j-i)
      
    answer.append(0)
    return answer

print(solution([4,1,2,5,3]))