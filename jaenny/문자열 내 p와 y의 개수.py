def solution(s):
    answer = True
    
    s = s.lower()
    
    count_p = s.count('p')
    count_y = s.count('y')
    
    if count_p == count_y : return True
    else : return False
