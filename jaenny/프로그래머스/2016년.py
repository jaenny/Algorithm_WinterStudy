def solution(a, b):
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    
    if a == 1 or a == 4 or a == 7: # 금요일
        return day[(b+4)%7]
    elif a == 10 : #토요일
        return day[(b+5)%7]
    elif a == 3 or a == 11 : #화요일
        return day[(b+1)%7]
    elif a == 9 or a == 12 : #목요일
        return day[(b+3)%7]
    elif a == 2 or a == 8 : #월요일
        return day[(b)%7]
    elif a == 6 : #수요일
        return day[(b+2)%7]
    elif a == 5 : #일요일
        return day[(b+6)%7]