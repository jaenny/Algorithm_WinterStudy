from collections import deque
def solution(numbers):
    answer = ''

    numbers = list(map(str,numbers))
    numbers.sort()
    print(numbers)
    q = deque()
    nums = [[q,q] for _ in range(10)]
    print(nums)

    for x in numbers :
      index = int(x[0])
      print(index)
      if int(x) % 10 == 0 or len(x) == 1 :
        nums[index][1].append(x)
      else :
        nums[index][0].appendleft(x)

    nums.reverse()
    for i in nums :
      print(i)

    for x in nums :
      if len(x[0]) > 0 :
        answer = answer + ''.join(x[0])
      if len(x[1]) > 0 :
        answer = answer + ''.join(x[1])
    return answer

print(solution([23, 232, 21, 212]))