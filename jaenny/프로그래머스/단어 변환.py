from collections import deque
def solution(begin, target, words):
  queue = deque()
  queue.append([begin,0])
  visit = [False]*len(words)

  while queue :
    word, cnt = queue.popleft()
    
    if word == target :
      return cnt
    
    for j in range(len(words)) :
      w = words[j]
      diffCnt = 0
      if not visit[j] :
        for i in range(len(w)) :
          if w[i] != word[i] : diffCnt += 1
          if diffCnt > 1 : break
        
        if diffCnt == 1 : 
          visit[j] = True
          queue.append([w,cnt+1])

  return 0

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog', 	["hot", "dot", "dog", "lot", "log"]))