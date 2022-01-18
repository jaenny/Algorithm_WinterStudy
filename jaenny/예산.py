def solution(d, budget):
    total = sum(d)
    while True :
        if total > budget :
            total = total - max(d)
            d.remove(max(d))
        else :
            return len(d)