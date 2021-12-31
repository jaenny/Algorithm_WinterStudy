def solution(nums):
    answer = -1
    res=[]
    from itertools import combinations
    for i in combinations(nums,3) :
        chk = sum(i)
        if isprime(chk) == 1 : res.append(chk)
    answer = len(res)
    return answer

def isprime(n) :
    import math
    for i in range(2,int(math.sqrt(n))+1) :
        if n % i == 0 : return 0
    return 1