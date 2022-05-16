from collections import defaultdict
def solution(msg):
  answer = []

  dic = defaultdict(int)

  idx = 1
  for alpha in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :
    dic[alpha] = idx
    idx += 1
  
  while msg :
    # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾기
    if len(msg) > 1 :
      for j in range(1,len(msg)+1) :
        w = msg[:j]
        if w not in dic :
          w = msg[:j-1]
          break
    else : w = msg

    answer.append(dic[w])

    if msg == w : 
      msg = ''
    else :
      wc = w + msg[len(w)] # c 추가
      dic[wc] = idx
      idx += 1
      msg = msg[len(w):]

  return answer

print(solution('ABABABABABABABAB'))