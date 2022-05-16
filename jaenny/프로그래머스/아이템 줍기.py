from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    matrix = [[0]*101 for i in range(101)]

    cX, cY, iX, iY = 2*characterX, 2*characterY, 2*itemX, 2*itemY

    d = [[1,0],[0,1],[-1,0],[0,-1]]

    visit = [[False]*101 for i in range(101)]
    visit[cX][cY] = 1

    queue = deque()
    queue.append([cX, cY])

    # 사각형 테두리 1로 만들기
    for x1, y1, x2, y2 in rectangle :
      for i in range(2*x1, 2*x2+1) :
        for j in range(2*y1, 2*y2+1) :
          matrix[i][j] = 1
    
    # 사각형 내부는 0으로 만들기
    for x1, y1, x2, y2 in rectangle :
      for i in range(2*x1+1, 2*x2) :
        for j in range(2*y1+1, 2*y2) :
          matrix[i][j] = 0
    
    # bfs 탐색
    while queue :
      x, y = queue.popleft()

      if (x, y) == (iX, iY) :
        answer = (matrix[x][y] - 1)//2
        break

      for dx, dy in d :
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 101 and 0 <= ny < 101 and matrix[nx][ny] == True and visit[nx][ny] == False :
          matrix[nx][ny] = matrix[x][y] + 1
          visit[nx][ny] = True
          queue.append([nx, ny])
        
    return answer

print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)) # 17