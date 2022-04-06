import math as Math
def solution(n):
    if Math.sqrt(n)  == int(Math.sqrt(n)) :
        return (int(Math.sqrt(n))+1)**2
    else :
        return -1
    