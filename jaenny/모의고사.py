def solution(answers):
    answer = []
    
    #1번 수포자
    one = [1,2,3,4,5]
    oneScore = 0
    for i in range(1,len(answers)+1) :
        if one[(i-1)%len(one)] == answers[i-1] : oneScore += 1
    
    #2번 수포자
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    twoScore = 0
    for i in range(1,len(answers)+1) :
        if two[(i-1)%len(two)] == answers[i-1] : twoScore += 1
            
    #3번 수포자
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    threeScore = 0
    for i in range(1,len(answers)+1) :
        if three[(i-1)%len(three)] == answers[i-1] : threeScore += 1
    
    maxScore = max(oneScore,twoScore,threeScore)

    if maxScore == oneScore : answer.append(1)
    if maxScore == twoScore : answer.append(2)
    if maxScore == threeScore : answer.append(3)
    
    return answer