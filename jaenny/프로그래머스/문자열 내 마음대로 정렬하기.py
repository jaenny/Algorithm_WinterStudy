def solution(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings