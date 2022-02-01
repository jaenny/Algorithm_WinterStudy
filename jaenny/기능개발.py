def solution(progresses, speeds):
    answer = []
    left = []
    for i in range(len(speeds)) :
      temp = (100 - progresses[i])/speeds[i]

      if temp != int(temp) :
        left.append(int(temp)+1)
      else :
        left.append(int(temp))

    maxl = left[0]
    count = 0
    for i in range(len(speeds)) :
      if maxl < left[i] :
        maxl = left[i]
        answer.append(count)
        count = 1
      else :
        count += 1
      if i == len(speeds)-1 :
        answer.append(count)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))