from collections import Counter
def solution(str1, str2):

  answer = 0
  str1 = str1.lower()
  str2 = str2.lower()

  # 집합 A, 집합 B 만들기
  A = []
  B = []
  for i in range(len(str1)-1) :
    word = str1[i:i+2]
    if word.isalpha() :
      A.append(word)
  for i in range(len(str2)-1) :
    word = str2[i:i+2]
    if word.isalpha() :
      B.append(word)
  
  Acount = Counter(A)
  Bcount = Counter(B)

  intersect = []
  union = []
  keys = set(Acount.keys()).union(set(Bcount.keys()))
  
  for key in keys :
    # 교집합 찾기
    if key in Acount and key in Bcount :
      intersectCount = min(Acount[key], Bcount[key])
      for i in range(intersectCount) :
        intersect.append(key)
    # 합집합 찾기
    unionCount = max(Acount[key], Bcount[key])
    for i in range(unionCount) :
      union.append(key)
  
  if len(union) == 0 : res = 1
  else :
    res = len(intersect)/len(union)

  return int(res*65536)

print(solution('FRANCE', 	'french'))


