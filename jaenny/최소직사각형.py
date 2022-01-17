def solution(sizes):
    answer = 0
    
    maxw, maxh = sizes[0]
    for size in sizes :
        w, h = size
        tempw = max(w,maxw)
        temph = max(h, maxh)
        tempr = tempw*temph
        
        h, w = size
        temprw = max(w,maxw)
        temprh = max(h, maxh)
        temprr = temprw*temprh
        
        if tempr <= temprr :
            maxw = tempw
            maxh = temph
            answer = tempr
        else:
            maxw = temprw
            maxh = temprh
            answer = temprr
        
    return answer