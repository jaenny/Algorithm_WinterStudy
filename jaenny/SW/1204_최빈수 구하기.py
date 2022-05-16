T = int(input())

for t in range(1,T+1) :
  board = [0]*101
  n = int(input())
  scores = list(map(int,input().split()))

  for score in scores :
    board[score] += 1
  
  maxCount = max(board)
  board.reverse()
  maxCountIndex = board.index(maxCount)

  print("#%d %d" %(t, 100-maxCountIndex))