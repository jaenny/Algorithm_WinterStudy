from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
  answer = []
  dic = defaultdict(list)

  for inf in info :
    inf = inf.split()

    condition = inf[:-1]
    score = int(inf[-1])

    for r in range(5) :
      case = list(combinations([0,1,2,3], r))
      for c in case :
        con = condition.copy()
        for idx in c :
          con[idx] = '-'
        con = ''.join(con)
        dic[con].append(score)
    
  for value in dic.values() :
    value.sort()

  for i in range(len(query)):
    q = query[i]
    q = q.replace('and ', '').split()
    qscore = int(q[-1])
    qcon = ''.join(q[:-1])
    count = 0
    if qcon in dic :
      target_list = dic[qcon]
      idx = bisect_left(target_list, qscore)
      count = len(target_list) - idx
    answer.append(count)
  return answer




# def solution(info, query):
#   answer = [0]*len(query)
#   query = [x.replace('and ','').split() for x in query]
#   info = [x.split() for x in info]

#   for i in range(len(query)) :
#     qlang, qpart, qjs, qfood, qscore = query[i]
    
#     for j in range(len(info)) :
#       lang, part, js, food, score = info[j]

#       if int(score) >= int(qscore) and qlang in ['-',lang] and qpart in ['-',part] and qjs in ['-',js] and qfood in ['-',food]:
#         answer[i] += 1
    
#   return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))