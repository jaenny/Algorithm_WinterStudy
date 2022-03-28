def solution(arr, brr):
  answer = 0

  # 제일 왼쪽
  if arr[0] != brr[0] :
    answer += 1
    diff = arr[0] - brr[0]
    arr[1] += diff
    arr[0] = brr[0]
  # 제일 오른쪽
  if arr[-1] != brr[-1] :
    answer += 1
    diff = arr[-1] - brr[-1]
    arr[-2] += diff
    arr[-1] = brr[-1]

  # 그 사이
  for i in range(1,len(arr)-1) :
    if arr[i] == brr[i] : continue
    else :
      answer += 1
      diff = arr[i] - brr[i]
      arr[i+1] += diff
      arr[i] = brr[i]
    # print(arr)

  return answer

print(solution([3,6,5,2,4], [4,5,4,5,2]))
print(solution([6,2,2,6], [4,4,4,4]))