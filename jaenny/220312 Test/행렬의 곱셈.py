def solution(arr1, arr2):
  answer = [[0]*len(arr[2]) for _ in range(len(arr1))]

  for i in range(len(answer)) :
    for j in range(len(answer[i])) :
      for k in range(len(arr1[i])) :
        answer[i][j] += arr1[i][k]*arr2[k][j]

  return answer