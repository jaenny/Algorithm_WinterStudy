count = 0
def go(temp, index, now, numbers,a, n, target) :
  if index == n:
    if now == target :
      temp.append(a)
      return
    else :
      return

  a[index] = numbers[index] # plus
  go(temp, index+1, sum(a), numbers,a, n, target)

  a[index] = -numbers[index] # minus
  go(temp, index+1, sum(a), numbers,a, n, target)

def solution(numbers, target):
  answer = 0

  a = [0]*len(numbers)
  temp = []
  go(temp, 0,0,numbers,a,len(numbers),target)

  return len(temp)





print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1],4))