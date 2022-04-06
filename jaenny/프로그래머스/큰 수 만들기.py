def solution(number, k):
  result = ''
  final = len(number) - k
  prev = 0
  i = 0
  while True :
    if len(result) == final :
      return result

    # 최댓값을 찾을 부분만 떼오기
    temp = number[:len(number)+1 - final+i]
    
    maxNum = 0 # 최댓값
    maxIndex = 0 # 최댓값의 인덱스
    for j in range(len(temp)) :
      if maxNum < int(temp[j]) :
        maxNum = int(temp[j])
        maxIndex = j

        # Case 10에서 시간초과가 되지 않으려면 반드시 추가해 주어야 한다!
        if maxNum == 9 : break 
    
    result += str(maxNum)
    prev = maxIndex + 1
    i += 1
    number = number[prev:]

print(solution('1924', 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))