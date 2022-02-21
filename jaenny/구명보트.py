from collections import deque
def solution(people, limit):
  answer = 0

  people.sort() # 정렬
  people = deque(people)

  while people :
    first = people[0] # 제일 가벼운 사람
    end = people[-1] # 제일 무거운 사람

    # 제일 가벼운 사람과 제일 무거운 사람을 매치해 구명보트에 태움
    if len(people)>=2 and first + end <= limit :
      people.popleft()
      people.pop()
    else : # 둘을 같이 태울 수 없다면 무거운 사람만 구명보트 하나에
      people.pop()
    answer += 1

  return answer

print(solution([20,40,50,80,90],100))
print(solution([70,50,80],100))