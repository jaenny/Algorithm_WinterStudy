from itertools import permutations
from math import inf
n = int(input())
arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

op = '+'*plus + '-'*minus + '*'*mul + '/'*div
op = list(map(str, op))

_max = -inf
_min = inf

for p in set(permutations(op)) :
    res = arr[0]
    for i in range(n-1) :
        op = p[i]
        nextNum = arr[i+1]

        if op == '+' :
            res = res + nextNum
        elif op == '-' :
            res = res - nextNum
        elif op == '*' :
            res = res * nextNum
        elif op == '/' :
            if res < 0 :
                res = -1*( abs(res) // nextNum )
            else :
                res = res // nextNum

    _max = max(_max, res)
    _min = min(_min, res)

print(_max)
print(_min)

