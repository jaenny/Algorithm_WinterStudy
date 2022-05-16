def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        arr1[i] = '0'*(n - len(str(bin(arr1[i])[2:])))+str(bin(arr1[i])[2:])
        arr2[i] = '0'*(n - len(str(bin(arr2[i])[2:])))+str(bin(arr2[i])[2:])

    for i in range(n) :
        line = ''
        for j in range(n) :
            if arr1[i][j] == '0' and arr2[i][j] == '0' : line += ' '
            else : line += '#'
        answer.append(line)
    return answer

print(solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28]))