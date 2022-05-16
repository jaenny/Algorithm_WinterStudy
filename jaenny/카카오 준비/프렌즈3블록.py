def solution(m, n, board):
  answer = 0

  board = [list(map(str,board[i])) for i in range(m)]
  di = [-1,-1,0,0]
  dj = [-1,0,-1,0]

  visit = [[0]*n for _ in range(m)]

  while True :
    ispop = False # 지워질 블록이 있나요?

    # 지워질 블록 찾기
    for i in range(1,m) :
      for j in range(1,n) :
        flag = True # 같다
        pattern = board[i][j]
        if pattern != 0 :
          # 사각형이 같은 모양들인지 확인
          for d in range(4) :
            ni = i + di[d]
            nj = j + dj[d]

            if board[ni][nj] != pattern :
              flag = False
              break
          if flag :
            for d in range(4) :
              ni = i + di[d]
              nj = j + dj[d]
              visit[ni][nj] = 1
              ispop = True

    # 더이상 지워질 블록이 없다면 answer 반환
    if ispop == False : return answer 

    # 위에서부터 한 칸씩 내리기
    for i in range(m) :
      for j in range(n) :
        if visit[i][j] == 1 :
          answer += 1
          # 맨 윗 줄일 경우
          if i == 0 :
            visit[i][j] = 0
            board[i][j] = 0
          # 아닐 경우
          else :
            visit[i][j] = 0
            for k in range(i, 0,-1) :
              board[k][j] = board[k-1][j]
              board[k-1][j] = 0

  return answer

print(solution(6, 6, 	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))