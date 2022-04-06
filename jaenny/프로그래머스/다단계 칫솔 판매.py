def solution(enroll, referral, seller, amount):
  answer = []

  # key : child, value : parent
  tree = {'-' : 'root'}
  sell = {'-' : 0}
  for i in range(len(enroll)) :
    child = enroll[i]
    parent = referral[i]
    sell[child] = 0
    tree[child] = parent

  for i in range(len(seller)) :
    child = seller[i]
    parent = tree[child]
    money = amount[i]*100
    sell[child] += money

    while True : # 루트까지 타고 올라가기
      benefit = money // 10
      sell[child] -= benefit
      sell[parent] += benefit

      child = parent
      parent = tree[child]
      money = benefit
      if parent == 'root' or money == 0: 
        break
  
  for person in enroll :
    answer.append(sell[person])

  return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))