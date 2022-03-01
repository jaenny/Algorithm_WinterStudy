def solution(n, left, right):
  answer = []
  
  for k in range(int(left), int(right)+1): # left와 right을 int로 감싸주지 않으면 TC 12,13이 런타임에러가 난다.
    num = max(k//n, k%n) + 1
    answer.append(num)
  return answer

print(0//2, 0//3, 0%3)
print(solution(4,7,14))