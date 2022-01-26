def solution(s):
    answer = []
    
    c = 1
    for i in range(len(s)) :
        if s[i] == ' ' :
            answer.append(' ')
            c = 1
        else :
            if (c)%2 == 1 :
                answer.append(s[i].upper())
            else :
                answer.append(s[i].lower())
            c+=1
    return ''.join(answer)