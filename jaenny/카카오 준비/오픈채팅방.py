def solution(records):
  answer = []

  people = dict()

  for record in records :
    record = record.split()
    op, id = record[0], record[1]
    if op != 'Leave' : name = record[2]

    if op == 'Enter' :
      people[id] = name
      text = id+' 님이 들어왔습니다.'
      answer.append(text)
    elif op == 'Change' :
      people[id] = name
    else :
      text = id+' 님이 나갔습니다.'
      answer.append(text)

  for i in range(len(answer)) :
    id, t1, t2 = answer[i].split()

    id = people[id]
    answer[i] = id+t1+' '+t2

  return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))