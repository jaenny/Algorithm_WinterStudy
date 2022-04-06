def solution(dirs):
  dr = 'UDRL'
  dk = 'DULR'
  answer = 0
  visited = [[[False]*4 for _ in range(11)] for _ in range(11)]

  i, j = 5, 5 # 출발지 설정 (0,0)

  for dir in dirs :
    d = dr.index(dir)
    k = dk.index(dir)
    ni, nj = i, j
    flag = True

    if d == 0 : ni = i - 1
    elif d == 1 : ni = i + 1
    elif d == 2 : nj = j + 1
    elif d == 3 : nj = j - 1

    if not visited[i][j][d] : 
      visited[i][j][d] = True
      flag = False

    if 0 <= ni <= 10 and 0 <= nj <= 10 :
      visited[ni][nj][k] = True
      i, j = ni, nj
      if flag == False :
        answer += 1
    else :
      continue
  return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))