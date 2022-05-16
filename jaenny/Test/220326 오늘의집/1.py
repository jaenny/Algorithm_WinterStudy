from collections import deque
def solution(rounds) :
  answer = 0
  before = []
  people = ['a','b','c','d']
  temp = [0,0,0,0] 
  for round in rounds :
    couples = deque()
    point = {'a':0, 'b': 0, 'c': 0, 'd': 0}

    for i in range(4) :
      point[people[i]] = round[i]

    for i in range(4) :
      if round[i] == people[i] : # 내가 날 지목 -> 규칙 위반 
        temp[i] += 1
      elif [people[i], point[people[i]]] in before or [point[people[i]], people[i]] in before  :
        temp[i] += 1
      elif people[i] == point[round[i]] : # 쌍방 지목
        couples.append([point[people[i]], point[round[i]]])
    before = next

  return sum(temp)

print(solution([["b", "a", "a", "d"], ["b", "c", "a", "c"], ["b", "a", "d", "c"]]))
print(solution([["b", "a", "d", "c"],["b", "a", "c", "d"]]))
print(solution([["b", "a", "d", "c"],["d", "c", "b", "a"],["b", "a", "d", "c"]]))
print(solution([["d", "a", "a", "a"],["c", "a", "a", "a"],["b", "a", "a", "a"]]	))