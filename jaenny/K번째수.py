def solution(array, commands):
    answer = []
    
    for command in commands :
        i,j,k = command
        arr = array.copy()
        arr = sorted(arr[i-1:j])
        answer.append(arr[k-1])
    
    return answer