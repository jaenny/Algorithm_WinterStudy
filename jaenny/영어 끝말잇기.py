def solution(n, words):
  prev = words[0]

  cnt = 1
  words_check = [words[0]]

  for i in range(1,len(words)) :
    # 이전 단어와 끝말잇기가 되지 않거나, 이미 언급한 단어일 경우
    if prev[-1] != words[i][0] or words[i] in words_check :
      if (i+1) % n == 0 : 
        return [n, cnt]
      else : 
        return [(i+1) % n, cnt]
      
    else :
      words_check.append(words[i])
      prev = words[i]
      if (i+1) % n == 0 : 
        cnt += 1
      
  return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))