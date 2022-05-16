def solution(S) :

  arr = []
  arr.append([S[0]])

  for i in range(1, len(S)) :
    word = S[i]
    new = []
    for j in range(len(arr)) :
      prev = arr[j]

      if word in prev[-1] :
        # 마지막꺼에 있으면 새로 추가
        temp = prev + [word]
        new.append(temp)
      else :
        # 마지막꺼에 없으면
        # 새로 추가 
        temp = prev + [word]
        new.append(temp)
        # 혹은 전에꺼에 추가
        prev[-1] = prev[-1] + word
        new.append(prev)
    arr = new
    print(word, arr)
    
  arr.sort(key=lambda x : len(x))
  _minlen = len(arr[0])
  cnt = 0
  for a in arr :
    if len(a) == _minlen : cnt += 1
    else : break

  return cnt

print(solution('cycle'))