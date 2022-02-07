from itertools import permutations #순열

# 소수 판정
def primeCheck(n) :
  if n < 2 :
    return False
  
  i = 2
  while i*i <= n :
    if n % i == 0 :
      return False
    i+=1
  
  return True


def solution(numbers):
    answer = 0

    numbers = list(map(str,numbers))

		# 만들 수 있는 숫자 순열 리스트 생성
    b =[]
    for j in range(1,len(numbers)+1) : # nPr : r은 1~numbers의 길이까지
      for i in list(permutations(numbers, j)):
          b.append(int(''.join(i)))
    b = list(set(b)) # 중복 숫자 제거

    for x in b :
      if primeCheck(x) == True :
        answer += 1

    return answer