def solution(name):
    answer = 0

    basis = 'ABCDEFGHIJKLMN'

    current = 0

    for i in range(len(name)) :
      if name[i] == 'A' :
        continue
      
      
      # 왼/오 이동
      answer += min(abs(i-current), len(name) - abs(i-current))
      current = i
      

      if name[i] in basis :
        answer += ord(name[i]) - 65
      else :
        answer += 91 - ord(name[i])
      print(current, answer)

    return answer

print(solution("ABAAAAAAAAABB"))