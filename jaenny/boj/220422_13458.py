n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
answer += len(people) # 총 감독관은 꼭 한 명씩 들어감

for i in range(len(people)) :
    people[i] -= b
    if people[i] < 0 :
        people[i] = 0
    else:
        answer += people[i] // c
        if people[i] % c != 0 : answer += 1
print(answer)
