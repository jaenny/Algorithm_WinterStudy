from collections import deque 
def solution(numstrs, words) :
  answer = [0]*len(words)
  translate = [['O','()'],['I'],['Z','S','7_'],['E', 'B'],['A'],['Z','S'],['b','G'],['T','Y'],['B','E3'],['g','q']]


  i = 0
  for idx, word in enumerate(words) :
    queue = deque()
    queue.append(['','',0]) # 바꾼 단어, 숫자
    temp = []
    while queue :
      pword, pnum,i = queue.popleft()
      # print(pword, pnum)
      if len(pnum) == len(word) :
        temp.append(pword)
        continue

      now = translate[int(word[i])]
      for n in now :
        if int(word[i]) == 5 and n == 'Z' :
          if '2' in pnum and 'Z' in pword : continue
          else :
            queue.append([pword+'Z',pnum+'5',i+1])
        elif int(word[i]) == 5 and n == 'S' :
          if '2' in pnum and 'S' in pword :
            continue
          else :
            queue.append([pword+'S', pnum+'5',i+1])
        elif word[i] == '2' and n == 'Z' :
          if '5' in pnum and 'Z' in pword :
            continue
          else :
            queue.append([pword+'Z', pnum+'2',i+1])
        elif word[i] == '2' and n == 'S' :
          if '5' in pnum and 'S' in pword :
            continue
          else :
            queue.append([pword+'S', pnum+'2',i+1])
        else :
          queue.append([pword+n, pnum+word[i],i+1])

    for t in temp :
      for str in numstrs :
        if t in str :
          answer[idx] += 1

  return answer

print(solution(["ZASSETE", "S4Z537B", "7_ASZEYB"],["2455373", "425", "373", "378"] ))