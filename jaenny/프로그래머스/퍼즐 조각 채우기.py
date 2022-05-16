from collections import deque
def solution(game_board, table):
  answer = 0
  n = len(game_board)

  def bfs(i,j,y,x) :
    queue = deque()
    queue.append([i, j, y, x])
    visit[i][j] = True
    cnt = 1

    dy = [1,-1,0,0]
    dx = [0,0,1,-1]

    while queue :
      i, j, y, x = queue.popleft()

      for dr in range(4) :
        ni = i + dy[dr]
        nj = j + dx[dr]
        ny = y + dy[dr]
        nx = x + dx[dr]
        
        if ni < 0 or ni >= n or nj < 0 or nj >= n : continue
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue

        if game_board[ni][nj] == 0 and table[ny][nx] == 1 and visit[ni][nj] == False :
          print("cnt추가",ni,nj,ny,nx)
          queue.append([ni,nj,ny,nx])
          visit[ni][nj] = True
          cnt += 1
        elif game_board[ni][nj] == 0 and table[ny][nx] == 0 and visit[ni][nj] == False: 
          return False
        print(queue)
    print("cnt:",cnt)
    return cnt
    


  # game_board
  for i in range(n) :
    for j in range(n) :
      # table
      for y in range(n-i) :
        for x in range(n-j) :
          # 회전
          # for d in range(4) :
          print(i,j,y,x)
          visit = [[False]*n for _ in range(n)]
          # if d == 0 :
          if game_board[i][j] == 0 and table[y][x] == 1 and visit[y][x] == False :
            a = bfs(i,j,y,x)
            if a : 
              answer += a
              print(answer)

  return answer

# print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
print(solution([[1,1,0],[0,1,0],[0,1,0]], [[1,0,1],[1,0,1],[1,0,0]]))