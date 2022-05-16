def solution(numbers, hand) :
  phone = {
    0 : [3,1],
    1 : [0,0],
    2 : [0,1],
    3 : [0,2],
    4 : [1,0],
    5 : [1,1],
    6 : [1,2],
    7 : [2,0],
    8 : [2,1],
    9 : [2,2]
  }

  L = [3,0] # '*' 위치
  R = [3,2] # '#' 위치

  Ls = [1,4,7]
  Rs = [3,6,9]

  answer = ''

  for num in numbers :
    if num in Ls :
      answer += 'L'
      L = phone[num]
    elif num in Rs :
      answer += 'R'
      R = phone[num]
    else :
      for n in range(10) :
        if n == num :
          # 거리체크
          Ldistance = abs(L[0] - phone[num][0]) + abs(L[1] - phone[num][1])
          Rdistance = abs(R[0] - phone[num][0]) + abs(R[1] - phone[num][1])

          if Ldistance < Rdistance :
            answer += 'L'
            L = phone[num]
          elif Ldistance > Rdistance :
            answer += 'R'
            R = phone[num]
          else :
            if hand == 'right' : 
              answer += 'R'
              R = phone[num]
            else :
              answer += 'L'
              L = phone[num]
          break
  return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))