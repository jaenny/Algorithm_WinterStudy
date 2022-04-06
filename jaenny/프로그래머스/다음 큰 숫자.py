def solution(n):
  answer = 0
  cur = bin(n)
  next = n

  while True :
    next_bin = bin(next+1)

    if cur.count('1') == next_bin.count('1') :
      return next+1
    else :
      next += 1

print(solution(78))
print(solution(15))